from selenium import webdriver
import time


def take_data():
    browser = webdriver.Chrome()

    # browser.get("https://e-university.tu-sofia.bg/ETUS/studenti/")
    browser.get("file:///D:/gitRepositories/University-Grades-Statistics-App/content0.html")

    # print("Fill the necessary data and log in, then navigate to grades section. Click enter when you done.")
    # input()

    time.sleep(1)

    html = browser.page_source

    browser.close()

    return html
