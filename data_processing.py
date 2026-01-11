import re
from bs4 import BeautifulSoup
import web_scraping
import pandas

# Configure pandas display settings
pandas.set_option("display.max_columns", None)
pandas.set_option("display.max_rows", None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)


def get_year(semester):
    if semester == 1 or semester == 2:
        return 1
    elif semester == 3 or semester == 4:
        return 2
    elif semester == 5 or semester == 6:
        return 3
    else:
        return 4


def filter_duplicate_grades(data_frame):
    rows_to_drop = []
    
    # Group by Subject AND Examination to find duplicates
    grouped = data_frame.groupby(["Subject", "Examination"])
    
    for (subject, exam_form), group in grouped:
        # Only process if examination form is 'Текуща оценка' or 'Изпит'
        if exam_form in ["Текуща оценка", "Изпит"]:
            if len(group) > 1:  # Only if there are multiple entries for this subject+exam combination
                grades = group["Grade"].values
                indices = group.index.values
                
                # Check if there's any grade > 2
                grades_above_2 = [g for g in grades if g > 2]
                
                if grades_above_2:
                    # Keep only the grade > 2 (should be the last/latest one)
                    grade_to_keep = max(grades_above_2)
                    # Drop all entries except the one with grade > 2
                    for idx in indices:
                        if data_frame.loc[idx, "Grade"] != grade_to_keep:
                            rows_to_drop.append(idx)
                else:
                    # All grades are <= 2, keep only one grade of 2
                    # Drop all but the first occurrence
                    first_kept = False
                    for idx in indices:
                        if not first_kept:
                            first_kept = True
                        else:
                            rows_to_drop.append(idx)
    
    # Drop the identified rows
    data_frame = data_frame.drop(rows_to_drop)
    
    return data_frame


def get_data_in_frame():
    raw_data = BeautifulSoup(web_scraping.take_data(), "html.parser")
    
    # Extract student name from the input field with id="izh"
    student_name_tag = raw_data.find("input", {"id": "izh"})
    student_name = student_name_tag.parent.get_text(strip=True).replace(student_name_tag.get_text(strip=True), '').strip() if student_name_tag else "Unknown"
    
    first_level_filtered_data = raw_data.find_all("tr")

    subject_data_pattern = r'<b>(.*?)<\/b><\/span>\s*\((.*?)\),.*<i>(.*?)<\/i>'
    semester_pattern = r'<b>(.*?)<\/b>'
    grade_pattern = r'\((\d+)\)\s*\(([\w\s]+)\)'

    semester_count = 1
    subjects = []
    years = []
    semesters = []
    examinations = []
    grades = []
    sessions = []

    for tag in first_level_filtered_data:
        match = re.search(subject_data_pattern, str(tag), re.DOTALL)

        if match:
            raw_grade_data = list(match.group(3).split("<br/>"))

            for index in raw_grade_data:
                grade_match = re.search(grade_pattern, str(index), re.DOTALL)

                if grade_match:
                    subjects.append(str(match.group(1)))
                    years.append(int(get_year(semester_count)))
                    semesters.append(int(semester_count))
                    examinations.append(str(match.group(2)))
                    grades.append(int(grade_match.group(1)))
                    sessions.append(str(grade_match.group(2)))
                else:
                    continue
        else:
            match_semester = re.search(semester_pattern, str(tag), re.DOTALL)

            if match_semester:
                try:
                    semester_count = int(match_semester.group(1)[0])
                except:
                    continue

    data = {
        "Subject": subjects,
        "Year": years,
        "Semester": semesters,
        "Examination": examinations,
        "Grade": grades,
        "Session": sessions
    }
    
    return {
        "Student": student_name,
        "Data": pandas.DataFrame(data)
    }
