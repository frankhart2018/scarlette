from typing import List
import os
from selenium import webdriver

from ...constants import GITHUB_CREDS_FILE
from ...errors import config_file_not_found
from .github_task import GithubTask
from .github_two_factor import GithubTwoFactor


class GithubLogin(GithubTask):
    def __init__(self) -> None:
        credentials: List[str] = self.__get_credentials()
        self.__username: str = credentials[0]
        self.__password: str = credentials[1]

        self.__url = "https://github.com/login"

    def __get_credentials(self) -> List[str]:
        if not os.path.exists(GITHUB_CREDS_FILE):
            raise config_file_not_found.ConfigFigleNotFound(
                message="GitHub credentials file missing, make sure you install it before using"
            )

        with open(GITHUB_CREDS_FILE, "r") as file:
            credentials: List[str] = file.read().split("\n")[:-1]

        return credentials

    def run(self, browser: webdriver.Chrome) -> None:
        browser.get(url=self.__url)

        username_field = browser.find_element_by_xpath("//input[@name='login']")
        password_field = browser.find_element_by_xpath("//input[@name='password']")

        username_field.send_keys(self.__username)
        password_field.send_keys(self.__password)

        login_button = browser.find_element_by_xpath("//input[@value='Sign in']")
        login_button.click()

        page_after_logging_in: str = browser.current_url

        if page_after_logging_in == "https://github.com/sessions/verified-device":
            github_two_factor: GithubTask = GithubTwoFactor()
            github_two_factor.run(browser=browser)