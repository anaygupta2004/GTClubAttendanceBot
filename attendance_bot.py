import time
from base import SeleniumBase

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AttendanceBot:
    def __init__(self):
        self.base = SeleniumBase(2)
        self.question_list = '//*[@id="question-list"]'
        self.attendance_link = "https://forms.office.com/r/8pvW3YZRFP"

    def open_form(self):
        # open in new tab:
        # self.base.driver.execute_script(f"window.open({self.attendance_link}, 'new_window')")
        # self.base.driver.switch_to.window(self.base.driver.window_handles[-1])

        self.base.driver.get(self.attendance_link)

    def fill_name(self, name):
        name_path = self.question_list + "/div[1]/div[2]/div/span/input"
        name_field = self.base.get_by_xpath(name_path)
        self.base.send_keys(name_field, name)

    def fill_club(self):
        club_path = self.question_list + "/div[2]/div[2]/div/div"
        club_field = self.base.get_by_xpath(club_path)
        club_field.click()

        program_team_field = self.base.get_by_text(
            "span", "Competitive Programming @ Tech"
        )
        program_team_field.click()

    def fill_major(self):
        major_path = self.question_list + "/div[3]/div[2]/div/div"
        major_field = self.base.get_by_xpath(major_path)
        major_field.click()

        coc_field = self.base.get_by_text("span", "College of Computing: CS")
        coc_field.click()

    def fill_in_person(self):
        in_person_path = self.question_list + "/div[4]/div[2]/div/div/div[1]/div"
        in_person_field = self.base.get_by_xpath(in_person_path)
        in_person_field.click()

    def submit(self, testing=False):
        submitButton = self.base.driver.find_element(
            By.CSS_SELECTOR, '[data-automation-id="submitButton"]'
        )
        if testing:
            time.sleep(0)
        else:
            submitButton.click()

    def formSequence(self, name):
        self.open_form()
        self.fill_name(name)
        self.fill_club()
        self.fill_major()
        self.fill_in_person()
        self.submit(False)
