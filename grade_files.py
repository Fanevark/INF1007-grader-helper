import os 
import re
import shutil 

from constants import OUTPUT_FOLDER, NUMERO_TP, GRADING_FOLDER

def get_grade_file(grading_directory: str, team_folder: str) -> tuple[str, str]: 
    team_number = team_folder.split("_")[0]
    team_path = os.path.join(grading_directory, team_folder)

    for file in os.listdir(team_path): 
        if file.endswith("grading.md"):
            return team_number, f"{team_path}/{file}"
    raise FileNotFoundError(f"Unable to find grading.md file in {team_path}")

def copy_grade_file(grade_file_path: str, destination: str):
    if OUTPUT_FOLDER not in os.listdir():
        os.makedirs(OUTPUT_FOLDER)
    shutil.copy2(grade_file_path, destination)

def extract_team_number_from_filename(filename: str): 
    return filename.split('-', 1)[1].split('.')[0]

def extract_grade_from_file(grade_file_path: str): 
    grade_line = ""
    with open(grade_file_path) as f: 
        for line in f: 
            match = re.search(r'\| *Total *\| .*', line)
            if match: 
                grade_line = line

    return float(grade_line.split("|")[2].replace(",", "."))

def extract_grade_files(): 
    for directory in os.listdir(GRADING_FOLDER):
        # Ignore hidden folders and files 
        if not directory.startswith(".") and os.path.isdir(f"{GRADING_FOLDER}/{directory}"):

            team_number, grade_file_path = get_grade_file(GRADING_FOLDER, directory)
            destination = f"{OUTPUT_FOLDER}/{NUMERO_TP}-{team_number}.md"
            if not os.path.exists(destination):
                copy_grade_file(grade_file_path, destination)
