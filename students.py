import os
import pandas as pd 

from constants import OUTPUT_FOLDER, CODE_ASSIGNMENT, SECTION_NUMBER, CORRECTOR_MAIL
import mail 
from grade_files import extract_team_number_from_filename, extract_grade_from_file, extract_name_from_filename

class StudentsData:
    def __init__(self, csv_path: str): 
        self.data = self.load_students(csv_path)
    
    def load_students(self, csv_path: str): 
        return pd.read_csv(csv_path)

    def populate_students_grade(self):
        if CODE_ASSIGNMENT.startswith("TP"):
            self.data[CODE_ASSIGNMENT] = None
            self.data[f'{CODE_ASSIGNMENT}-grade-file'] = None
            for file in os.listdir(OUTPUT_FOLDER): 
                if file.startswith(CODE_ASSIGNMENT):
                    team_number = extract_team_number_from_filename(file)
                    grade = extract_grade_from_file(f"{OUTPUT_FOLDER}/{file}")
                    self.data.loc[self.data["Groupe"] == team_number, f"{CODE_ASSIGNMENT}"] = grade
                    self.data.loc[self.data["Groupe"] == team_number, f"{CODE_ASSIGNMENT}-grade-file"] = f"{OUTPUT_FOLDER}/{file}"
        else: 
            self.data[CODE_ASSIGNMENT] = None
            self.data[f'{CODE_ASSIGNMENT}-grade-file'] = None
            for file in os.listdir(OUTPUT_FOLDER): 
                if file.startswith(CODE_ASSIGNMENT):
                    student_name = extract_name_from_filename(file)
                    matricule = self.data[self.data["Nom de famille"].str.contains(student_name)]["Matricule"].values[0]
                    grade = extract_grade_from_file(f"{OUTPUT_FOLDER}/{file}")
                    self.data.loc[self.data["Matricule"] == matricule, f"{CODE_ASSIGNMENT}"] = grade
                    self.data.loc[self.data["Matricule"] == matricule, f"{CODE_ASSIGNMENT}-grade-file"] = f"{OUTPUT_FOLDER}/{file}"

    def send_mail_groups(self, send_mail: bool = True):
        emails = []
        if CODE_ASSIGNMENT.startswith("TP"):
            for group in self.data["Groupe"].unique():
                group_students = self.data[self.data["Groupe"] == group]
                file_path = group_students[f"{CODE_ASSIGNMENT}-grade-file"].tolist()[0]
                receivers = group_students["Adresse de courriel"].to_list()
                subject = f"Correction {CODE_ASSIGNMENT} - Groupe {group}"
                message = mail.create_message(group)

                print(f"Group {group}: {receivers}")
                attachments = [mail.MailAttachment("text/md", f"./{file_path}", f"{CODE_ASSIGNMENT}-{group}.md")]
                emails.append(mail.build_mail(CORRECTOR_MAIL, receivers, subject, message, attachments))
        else: 
            for index in self.data.index:
                student = self.data.loc[index]
                file_path = student[f"{CODE_ASSIGNMENT}-grade-file"]
                receiver = student["Adresse de courriel"]
                print(f"Student {student['Matricule']}: {receiver}")
                subject = f"INF1007 - Correction {CODE_ASSIGNMENT}"
                message = mail.create_message(student)
                attachments = [mail.MailAttachment("text/md", f"./{file_path}", f"{CODE_ASSIGNMENT}-{student["Matricule"]}.md")]
                emails.append(mail.build_mail(CORRECTOR_MAIL, [receiver], subject, message, attachments))

        if send_mail:
            mail.send_mails(emails)

    def save_csv(self):
        self.data.to_csv(f"INF1007-{SECTION_NUMBER}-{CODE_ASSIGNMENT}.csv")

    
