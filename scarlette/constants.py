from pathlib import Path
import os


INSTALLATION_DIR: str = os.path.join(str(Path.home()), ".scarlette")
GITHUB_CREDS_FILE: str = os.path.join(INSTALLATION_DIR, "github")

OPTIONS = """1. Github Repo Creator"""