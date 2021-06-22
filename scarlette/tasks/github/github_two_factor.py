from selenium import webdriver

from .github_task import GithubTask
from ...errors import invalid_verification_code


class GithubTwoFactor(GithubTask):
    def run(self, browser: webdriver.Chrome) -> None:
        verification_code: str = input("Enter verification code: ")

        if len(verification_code) != 6:
            raise invalid_verification_code.InvalidVerificationCode(message="Invalid GitHub verification code, should have 6 digits!")

        otp_field = browser.find_element_by_xpath("//input[@name='otp']")
        otp_field.send_keys(verification_code)

        verify_button = browser.find_element_by_xpath("//button[@class='btn btn-primary btn-block']")
        verify_button.click()