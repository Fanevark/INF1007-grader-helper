import students
import grade_files
from constants import STUDENTS_CSV_FILENAME

if __name__ == "__main__":
    students_data = students.StudentsData(STUDENTS_CSV_FILENAME)
    grade_files.extract_grade_files()    
    students_data.populate_students_grade()
    students_data.send_mail_groups()
    students_data.save_csv()