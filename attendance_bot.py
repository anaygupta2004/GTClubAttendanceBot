import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()

# Keep tabs open after program ends
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# github plug
# driver.get("https://github.com/akhilkammila")

attendance_link = "https://forms.office.com/pages/responsepage.aspx?id=u5ghSHuuJUuLem1_MvqggxAYDlX66f1Ho6k8B5xyijVUMDRHUUQzVU42Q0tKODFZN1ZGSjRNMThCRyQlQCN0PWcu"
question_list = '//*[@id="question-list"]'

def open_form():
    # Uncomment to open each form in a new tab (slower)
    # driver.execute_script("window.open('https://google.com', 'new_window')")
    # driver.switch_to.window(driver.window_handles[-1])
    
    driver.get(attendance_link)

def fill_name(name):
    name_path = question_list + '/div[1]/div[2]/div/span/input'
    name_field = driver.find_element(By.XPATH, name_path)
    name_field.clear()
    name_field.send_keys(name)

def fill_club():
    club_path = question_list + '/div[2]/div[2]/div/div'
    club_field = driver.find_element(By.XPATH, club_path)
    club_field.click()

    program_team_path = club_path + '/div[2]/div[18]/span[2]/span'
    program_team_field = driver.find_element(By.XPATH, program_team_path)
    program_team_field.click()

def fill_major():
    major_path = question_list + '/div[3]/div[2]/div/div'
    major_field = driver.find_element(By.XPATH, major_path)
    major_field.click()

    college_computing_path = major_path + '/div[2]/div[1]/span[2]/span'
    coc_field = driver.find_element(By.XPATH, college_computing_path)
    coc_field.click()

def fill_in_person():
    in_person_path = question_list + '/div[4]/div[2]/div/div/div[1]/div'
    in_person_field = driver.find_element(By.XPATH, in_person_path)
    in_person_field.click()

def submit(testing=True):
    submitButton = driver.find_element(By.CSS_SELECTOR, '[data-automation-id="submitButton"]')
    if testing: time.sleep(3)
    else: submitButton.click()

def formSequence(name):
    open_form()
    fill_name(name)
    fill_club()
    fill_major()
    fill_in_person()
    submit()

def read_names():
    names = []
    with open("names_list.txt") as f:
        name = f.readline().rstrip()

        while name:
            names.append(name)
            name = f.readline().rstrip()
    return names
    

if __name__ == "__main__":
    names = read_names()
    for name in names:
        formSequence(name)