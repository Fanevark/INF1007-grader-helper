import os 
from enum import Enum
from dotenv import load_dotenv

class PlatformType(Enum):
    MOODLE = "moodle"
    GITHUB = "github"

class AssignmentType(Enum):
    TP = "TP"
    PROJECT = "PR"

# Load environment variables from .env file
load_dotenv() 

def load_env_variable(var_name: str) -> str: 
    var = os.getenv(var_name)
    if var is None: 
        raise EnvironmentError(f"{var_name} is not set in .env file")
    return var

CODE_ASSIGNMENT = load_env_variable("CODE_ASSIGNMENT")

if CODE_ASSIGNMENT.startswith("TP"):
    ASSIGNMENT_TYPE = AssignmentType.TP
elif CODE_ASSIGNMENT.startswith("PR"):
    ASSIGNMENT_TYPE = AssignmentType.PROJECT

SECTION_NUMBER = load_env_variable("NUMERO_SECTION")
OUTPUT_FOLDER = f"./results/{CODE_ASSIGNMENT}-results"

TOTAL_SECTION_NUMBER = int(load_env_variable("TOTAL_SECTION_NUMBER"))


GRADING_FOLDER = load_env_variable("GRADING_FOLDER")

ASSIGNMENT_DATA_FOLDER = load_env_variable("ASSIGNMENT_DATA_FOLDER")
STUDENTS_CSV_FILENAME = load_env_variable("STUDENTS_CSV_FILENAME")

CORRECTOR_MAIL = load_env_variable("CORRECTOR_MAIL")
CORRECTOR_MAIL_USERNAME = load_env_variable("CORRECTOR_MAIL_USERNAME")
CORRECTOR_MAIL_PASSWORD = load_env_variable("CORRECTOR_MAIL_PASSWORD")

PLATFORM_TYPE = PlatformType(load_env_variable("PLATFORM_TYPE"))