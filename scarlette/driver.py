from .constants import OPTIONS
from .errors import invalid_option
from .tasks import pipeline


def run_scarlette():
    options = OPTIONS
    
    num_valid_operations = len(options.split("\n"))

    print(options + "\n")
    user_option = int(input("Select option: "))

    if user_option < 0 or user_option > num_valid_operations:
        raise invalid_option.InvalidOption(message=f"Invalid option, should be in range [1, {num_valid_operations}]")

    option_to_operation = {
        1: "github-repo-create",
    }

    pipeline.Pipeline.run(task=option_to_operation[user_option])