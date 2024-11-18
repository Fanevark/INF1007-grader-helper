import os 
import re
import shutil 
import pandas as pd
from constants import OUTPUT_FOLDER, CODE_ASSIGNMENT, GRADING_FOLDER, PLATFORM_TYPE, PlatformType
from prepare_projects import create_grade_file_from_readme

def get_grade_file(students_data: pd.DataFrame, grading_directory: str, team_folder: str) -> tuple[str, str]: 
    if PLATFORM_TYPE == PlatformType.MOODLE:
        team_number = team_folder.split("_")[0]
    else: 
        team_number = students_data[students_data["TP3 repository"] == team_folder]["Groupe"].values[0]

    team_path = os.path.join(grading_directory, team_folder)

    if not "correction.md" in os.listdir(team_path):
        if "README.md" in os.listdir(team_path):
            create_grade_file_from_readme(f"{team_path}/README.md", f"{team_path}/correction.md")

    if "correction.md" in os.listdir(team_path):
        return team_number, f"{team_path}/correction.md"
    raise FileNotFoundError(f"Unable to find correction/grading.md file in {team_path}")

def copy_grade_file(grade_file_path: str, destination: str):
    shutil.copy2(grade_file_path, destination)

def extract_name_from_filename(filename: str): 
    return filename.split('-', 1)[1].split('.', 1)[0].split(" ")[-1].replace("├й", "é").replace("├и", "è")

def extract_team_number_from_filename(filename: str) -> str: 
    return filename.split('-', 1)[1].split('.')[0]

def extract_grade_from_file(grade_file_path: str): 
    grade_line = ""
    with open(grade_file_path) as f: 
        for line in f: 
            match = re.search(r'Total', line)
            if match: 
                grade_line = line

    grade = float(grade_line.split("|")[2].replace(",", "."))
    if grade > 20: 
        return grade / 5
    return grade

def extract_grade_files(students_data: pd.DataFrame): 
    for directory in os.listdir(GRADING_FOLDER):
        # Ignore hidden folders and files 
        if not directory.startswith(".") and os.path.isdir(f"{GRADING_FOLDER}/{directory}"):
            team_number, grade_file_path = get_grade_file(students_data, GRADING_FOLDER, directory)
            if not os.path.exists(OUTPUT_FOLDER):
                os.makedirs(OUTPUT_FOLDER)
            destination = f"{OUTPUT_FOLDER}/{CODE_ASSIGNMENT}-{team_number}.md"
            if not os.path.exists(destination):
                copy_grade_file(grade_file_path, destination)
