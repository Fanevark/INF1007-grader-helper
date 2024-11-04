import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

def load_env_variable(var_name: str) -> str: 
    var = os.getenv(var_name)
    if var is None: 
        raise EnvironmentError(f"{var_name} is not set in .env file")
    return var

CODE_ASSIGNMENT = load_env_variable("CODE_ASSIGNMENT")
SECTION_NUMBER = load_env_variable("NUMERO_SECTION")
OUTPUT_FOLDER = f"./results/{CODE_ASSIGNMENT}-results"

GRADING_FOLDER = load_env_variable("GRADING_FOLDER")

ASSIGNMENT_DATA_FOLDER = load_env_variable("ASSIGNMENT_DATA_FOLDER")
STUDENTS_CSV_FILENAME = load_env_variable("STUDENTS_CSV_FILENAME")

CORRECTOR_MAIL = load_env_variable("CORRECTOR_MAIL")
CORRECTOR_MAIL_USERNAME = load_env_variable("CORRECTOR_MAIL_USERNAME")
CORRECTOR_MAIL_PASSWORD = load_env_variable("CORRECTOR_MAIL_PASSWORD")
