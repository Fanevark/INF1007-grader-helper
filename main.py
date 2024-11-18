import students
import grade_files
import prepare_projects
from constants import STUDENTS_CSV_FILENAME, GRADING_FOLDER, ASSIGNMENT_DATA_FOLDER, CODE_ASSIGNMENT

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="INF1007 Correction")
    parser.add_argument("-z", "--zip", help="Unzip projects", action="store_true")
    parser.add_argument("-f", "--filter", help="Filter projects", action="store_true")
    parser.add_argument("-g", "--grade", help="Grade projects", action="store_true")
    parser.add_argument("-p", "--prepare", help="Prepare projects", action="store_true")
    parser.add_argument("-s", "--send", help="Send grades", action="store_true")
    args = parser.parse_args()

    students_data = students.StudentsData(STUDENTS_CSV_FILENAME)


    # if args.zip:
    #     raise NotImplementedError("Unzip is not implemented")
    #     # TODO: DO
    #     # prepare_projects.unzip_moodle_archive()

    if args.prepare: 
        if args.filter: 
            prepare_projects.filter_projects(GRADING_FOLDER, students_data.matricules)
        prepare_projects.copy_data_files(GRADING_FOLDER, "./data/projet1_data/tests.py")
        prepare_projects.copy_grading_file(GRADING_FOLDER, f"./{ASSIGNMENT_DATA_FOLDER}/correction.md")
        prepare_projects.copy_vscode_config(GRADING_FOLDER, "./.vscode")

    if args.grade: 
        grade_files.extract_grade_files(students_data.data)    
        students_data.populate_students_grade()
        students_data.send_mail_groups(args.send)
        students_data.save_csv()