import re
from bs4 import BeautifulSoup
import web_scraping
import pandas


def get_year(semester):
    if semester == 1 or semester == 2:
        return 1
    elif semester == 3 or semester == 4:
        return 2
    elif semester == 5 or semester == 6:
        return 3
    else:
        return 4


def get_data_in_frame():
    raw_data = BeautifulSoup(web_scraping.take_data(), "html.parser")
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

    pandas.set_option("display.max_columns", None)
    pandas.set_option("display.max_rows", None)

    return pandas.DataFrame(data)
