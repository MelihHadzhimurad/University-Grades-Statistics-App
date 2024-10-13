import re

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re as regexBrowser
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=chrome_options)
browser = webdriver.Chrome(options=options)
# browser.get("https://e-university.tu-sofia.bg/ETUS/studenti/")
browser.get("file:///D:/gitRepositories/University-Grades-Statistics-App/content0.html")

"""
faculty_number_field = browser.find_element(By.XPATH, "//*[@id='fnum']")
faculty_number_field.send_keys(faculty_number)

time.sleep(1)

egn_field = browser.find_element(By.XPATH, "//*[@id='egn']")
time.sleep(1)
egn_field.click()
time.sleep(1)
egn_field.send_keys(egn)
time.sleep(1)

print("fill the text from the image")
input()

time.sleep(1)

login_button = browser.find_element(By.XPATH, "//*[@id='but']")
login_button.click()
time.sleep(1)

browser.find_element(By.XPATH, "//*[@id='desk']/u[3]").click()
time.sleep(1)
"""

html = browser.page_source

browser.close()

soup = BeautifulSoup(html, "html.parser")
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

