import re
from bs4 import BeautifulSoup
import web_scraping


def get_year(semester):
    if semester == 1 or semester == 2:
        return 1
    elif semester == 3 or semester == 4:
        return 2
    elif semester == 5 or semester == 6:
        return 3
    else:
        return 4


raw_data = BeautifulSoup(web_scraping.take_data(), "html.parser")
first_level_filtered_data = raw_data.find_all("tr")

subject_data_pattern = r'<b>(.*?)<\/b>.*<i>(.*?)<\/i>'
semester_pattern = r'<b>(.*?)<\/b>'
degree_pattern = r'\((\d+)\)\s*\((\w+)\)'

semester_count = 1
subjects = []
years = []
semesters = []
degrees = []
sessions = []

for tag in first_level_filtered_data:
    match = re.search(subject_data_pattern, str(tag), re.DOTALL)

    if match:
        # print(match.group(1) + " -- " + match.group(2))
        """
        subjects.append(match.group(1))
        years.append(get_year(semester_count))
        semesters.append(semester_count)
        """
        raw_degree_data = list(match.group(2).split("<br/>"))

        if raw_degree_data[0] == "oценка:":
            degree_match = re.search(degree_pattern, str(raw_degree_data[1]), re.DOTALL)
            if degree_match:
                print(match.group(1) + "|" + degree_match.group(1) + "|" + degree_match.group(2))
            else:
                continue
        else:
            for index in raw_degree_data:
                degree_match = re.search(degree_pattern, str(index), re.DOTALL)

                if degree_match:
                    print(match.group(1) + "|" + degree_match.group(1) + "|" + degree_match.group(2))
                else:
                    continue
    else:
        match_semester = re.search(semester_pattern, str(tag), re.DOTALL)

        if match_semester:
            try:
                # print(int(match_semester.group(1)[0]))
                semester_count = int(match_semester.group(1)[0])
                print(semester_count)
            except:
                continue

"""
semesterCounter = 0
sumOfGrades = 0
gradeCounter = 0
sumOfAllGrades = 0
counterForOverallGPA = 0

for grade in grades:
    sub_grade = str(grade)

    if regexBrowser.search(r'\b[1-8]\sсем\.', sub_grade):
        if regexBrowser.search(r'текущ', sub_grade):
            print("{} semester GPA: {:.2f}".format(semesterCounter, float(sumOfGrades / gradeCounter)))
            semesterCounter += 1
            sumOfAllGrades += sumOfGrades
            sumOfGrades = 0
            counterForOverallGPA += gradeCounter
            gradeCounter = 0
            break
        elif semesterCounter == 0:
            semesterCounter += 1
            continue
        else:
            print("{} semester GPA: {:.2f}".format(semesterCounter, float(sumOfGrades/gradeCounter)))
            semesterCounter += 1
            sumOfAllGrades += sumOfGrades
            sumOfGrades = 0
            counterForOverallGPA += gradeCounter
            gradeCounter = 0

    elif "<i>" in sub_grade:
        grade = regexBrowser.findall(r'\((?:[1-6])\)', sub_grade)
        sumOfGrades += int((grade[0])[1])
        gradeCounter += 1
    else:
        continue

print("Overall GPA to date: {:.2f}".format(float(sumOfAllGrades / counterForOverallGPA)))
"""


