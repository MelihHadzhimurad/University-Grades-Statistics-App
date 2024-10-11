from selenium import webdriver
import time
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
# import re as regexBrowser
from selenium.webdriver.chrome.options import Options

"""
faculty_number = str(input("Faculty Number: "))
egn = str(input("EGN: "))
"""

# chrome_options = Options()
# chrome_options.add_argument("--headless")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=chrome_options)
browser = webdriver.Chrome(options=options)
time.sleep(1)
browser.get("https://e-university.tu-sofia.bg/ETUS/studenti/")
# browser.get("file:///D:/gradeCalculator/content.html")
time.sleep(5)

browser.download_file('captcha.php', "C:\Users\user\downloads")
browser.implicitly_wait(5)
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
"""
html = browser.page_source

browser.close()

soup = BeautifulSoup(html, "html.parser")
grades = soup.find_all("tr")

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

