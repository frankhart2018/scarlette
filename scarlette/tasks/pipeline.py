from scarlette.tasks.github import github_repo_create
from typing import List, Type
import time


class Pipeline:
    @staticmethod
    def run(task: str) -> None:
        if task == "github-repo-create":
            from selenium import webdriver
            from webdriver_manager.chrome import ChromeDriverManager

            from .github import github_task, github_login

            browser: webdriver.Chrome = webdriver.Chrome(ChromeDriverManager().install())
            tasks: List[github_task.GithubTask] = [github_login.GithubLogin(), github_repo_create.GithubRepoCreate()]

            for current_task in tasks:
                current_task.run(browser=browser)

            browser.close()