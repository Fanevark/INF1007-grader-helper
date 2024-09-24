import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

NUMERO_TP = "TP1"
NUMERO_LAB = "L04"
OUTPUT_FOLDER = "output"

GRADING_FOLDER = "../correction"

STUDENTS_CSV_FILENAME = "INF1007-L04.csv"

CORRECTOR_MAIL = os.getenv("CORRECTOR_MAIL")
CORRECTOR_MAIL_USERNAME = os.getenv("CORRECTOR_MAIL_USERNAME")
CORRECTOR_MAIL_PASSWORD = os.getenv("CORRECTOR_MAIL_PASSWORD")

if CORRECTOR_MAIL is None:
    raise EnvironmentError("CORRECTOR_MAIL is not set in .env file")
if CORRECTOR_MAIL_USERNAME is None:
    raise EnvironmentError("CORRECTOR_MAIL_USERNAME is not set in .env file")
if CORRECTOR_MAIL_PASSWORD is None:
    raise EnvironmentError("CORRECTOR_MAIL_PASSWORD is not set in .env file")
