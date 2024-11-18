import os 
from shutil import rmtree, copyfile, copytree 
import zipfile
import re
from constants import GRADING_FOLDER, SECTION_NUMBER,  ASSIGNMENT_TYPE, AssignmentType


def unzip_moodle_archive(archive_path: str):
    with zipfile.ZipFile(archive_path, "r") as zip_ref:
        zip_ref.extractall(GRADING_FOLDER)

def filter_projects(directory: str, matricules: list[int] | None = None): 
    for file in os.listdir(directory):
        if ASSIGNMENT_TYPE == AssignmentType.TP:
            if not file.startswith(SECTION_NUMBER):
                rmtree(f"{directory}/{file}")
        elif ASSIGNMENT_TYPE == AssignmentType.PROJECT:
            matricule = int(file.split("_")[2])
            if matricule not in matricules:
                rmtree(f"{directory}/{file}")

def unzip_subdirectories(directory: str):
    for project_dir in os.listdir(directory): 
        for file in os.listdir(f"{directory}/{project_dir}"):
            if file.endswith(".zip"):
                with zipfile.ZipFile(f"{directory}/{project_dir}/{file}", "r") as zip_ref:
                    zip_ref.extractall(f"./{directory}/{project_dir}/")

def copy_grading_file(directory: str, grading_file_path: str| None = None, readme_file_path: str | None = None): 
    if grading_file_path is None and readme_file_path is None: 
        raise ValueError("You must provide a grading file or a readme file path")
    if readme_file_path is not None:
        grading_file_path = "./correction.md"
        create_grade_file_from_readme(readme_file_path, grading_file_path)

    for project_dir in os.listdir(directory): 
        copyfile(grading_file_path, f"{directory}/{project_dir}/correction.md")

def copy_data_files(directory: str, data_files_path: str): 
    for project_dir in os.listdir(directory):
        if os.path.isdir(f"{directory}/{project_dir}"):
            filename = data_files_path.split("/")[-1]
            copyfile(data_files_path, f"{directory}/{project_dir}/{filename}")

def copy_vscode_config(directory: str, vscode_config_path: str): 
    for project_dir in os.listdir(directory): 
        if os.path.isdir(f"{directory}/{project_dir}"):
            copytree(vscode_config_path, f"{directory}/{project_dir}/.vscode", dirs_exist_ok=True)

def create_grade_file_from_readme(readme_path: str, destination: str):
    content = extract_grade_file_content_from_readme(readme_path)
    with open(destination, "w") as f: 
        f.write(content)

# TODO: Optimize it is currently ugly
def extract_grade_file_content_from_readme(readme_path: str) -> str: 
    content = ""
    with open(readme_path) as f: 
        inside_bareme = False
        for line in f: 
            match = re.search(r'Barème', line)
            if match: 
                inside_bareme = True

            match = re.search(r'Annexe', line)
            if match: 
                inside_bareme = False

            if inside_bareme: 
                content += line

    return content 
