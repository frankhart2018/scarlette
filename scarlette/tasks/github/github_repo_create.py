from scarlette.errors.invalid_option import InvalidOption
from selenium import webdriver
import time

from .github_task import GithubTask


class GithubRepoCreate(GithubTask):
    def __init__(self) -> None:
        self.__repo_name: str = input("Enter repo name: ")
        self.__is_public: str = input("Is it public (y/n): ")

        if self.__is_public not in ['y', 'n']:
            raise InvalidOption(message="Valid options are 'y' and 'n'")

        self.__is_public = str(True) if self.__is_public == 'y' else str(False)
        self.__url: str = "https://github.com/new"

    def run(self, browser: webdriver.Chrome) -> None:
        browser.get(self.__url)

        repo_name_field = browser.find_element_by_xpath("//input[@id='repository_name']")
        repo_name_field.send_keys(self.__repo_name)

        if not bool(self.__is_public):
            repo_private_visibility_field = browser.find_element_by_xpath("//input[@id='repository_visibility_private']")
            repo_private_visibility_field.click()

        time.sleep(2)

        create_repo_button = browser.find_element_by_xpath("//button[@type='submit'][@class='btn btn-primary']")
        create_repo_button.click()