import os 
from shutil import rmtree, copyfile, copytree 
from constants import GRADING_FOLDER, SECTION_NUMBER
import zipfile

def unzip_moodle_archive(archive_path: str):
    with zipfile.ZipFile(archive_path, "r") as zip_ref:
        zip_ref.extractall(GRADING_FOLDER)

def filter_tps(directory: str): 
    for file in os.listdir(directory):
        if file.startswith(SECTION_NUMBER):
            rmtree(f"{directory}/{file}")

def filter_projects(directory: str, matricules: list[int]): 
    for file in os.listdir(directory):
        matricule = int(file.split("_")[2])
        if matricule not in matricules:
            rmtree(f"{directory}/{file}")

def unzip_files(directory: str):
    for project_dir in os.listdir(directory): 
        for file in os.listdir(f"{directory}/{project_dir}"):
            if file.endswith(".zip"):
                with zipfile.ZipFile(f"{directory}/{project_dir}/{file}", "r") as zip_ref:
                    zip_ref.extractall(f"./{directory}/{project_dir}/")

def copy_grading_file(directory: str, grading_file_path: str): 
    for project_dir in os.listdir(directory): 
        copyfile(grading_file_path, f"{directory}/{project_dir}/correction.md")

def copy_vscode_config(directory: str, vscode_config_path: str): 
    for project_dir in os.listdir(directory): 
        copytree(vscode_config_path, f"{directory}/{project_dir}/.vscode")
