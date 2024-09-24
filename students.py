import os
import pandas as pd 

from constants import OUTPUT_FOLDER, NUMERO_TP, NUMERO_LAB, CORRECTOR_MAIL
import mail 
from grade_files import extract_team_number_from_filename, extract_grade_from_file

class StudentsData:
    def __init__(self, csv_path: str): 
        self.data = self.load_students(csv_path)
    
    def load_students(self, csv_path: str): 
        return pd.read_csv(csv_path)

    def populate_students_grade(self):
        self.data[NUMERO_TP] = None
        self.data[f'{NUMERO_TP}-grade-file'] = None
        for file in os.listdir(OUTPUT_FOLDER): 
            if file.startswith(NUMERO_TP):
                team_number = extract_team_number_from_filename(file)
                grade = extract_grade_from_file(f"{OUTPUT_FOLDER}/{file}")
                self.data.loc[self.data["Groupe"] == team_number, f"{NUMERO_TP}"] = grade
                self.data.loc[self.data["Groupe"] == team_number, f"{NUMERO_TP}-grade-file"] = f"{OUTPUT_FOLDER}/{file}"

    def send_mail_groups(self):
        emails = []
        for group in self.data["Groupe"].unique():
            group_students = self.data[self.data["Groupe"] == group]
            file_path = group_students[f"{NUMERO_TP}-grade-file"].tolist()[0]
            receivers = group_students["Adresse de courriel"].to_list()
            subject = f"Correction {NUMERO_TP} - Groupe {group}"
            message = mail.create_message(group)

            print(f"Group {group}: {receivers}")
            attachments = [mail.MailAttachment("text/md", f"./{file_path}", f"{NUMERO_TP}-{group}.md")]
            emails.append(mail.build_mail(CORRECTOR_MAIL, receivers, subject, message, attachments))
        mail.send_mails(emails)

    def save_csv(self):
        self.data.to_csv(f"INF1007-{NUMERO_LAB}-{NUMERO_TP}.csv")
