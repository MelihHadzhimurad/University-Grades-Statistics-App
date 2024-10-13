import re
from bs4 import BeautifulSoup
import re as regexBrowser
import web_scraping


soup = BeautifulSoup(web_scraping.take_data(), "html.parser")
clearedSoup = soup.find_all("tr")

degree_pattern = r'<b>(.*?)<\/b>.*<i>(.*?)<\/i>'
semester_pattern = r'<b>(.*?)<\/b>'

for tag in clearedSoup:
    match = re.search(degree_pattern, str(tag), re.DOTALL)

    if(match):
        print(match.group(1) + " -- " + match.group(2))
    else:
        match_semester = re.search(semester_pattern, str(tag), re.DOTALL)

        if(match_semester):
            try:
                print(int(match_semester.group(1)[0]))
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

