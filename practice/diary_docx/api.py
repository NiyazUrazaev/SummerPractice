import os

from docxtpl import DocxTemplate

from SummerPractice.settings import BASE_DIR, MEDIA_ROOT


class DocxDiary():

    def __init__(self, student, teacher, practice, diary_days):
        self.doc = DocxTemplate(os.path.join(
            BASE_DIR, "practice/diary_docx/templates/diary_template.docx"))
        self.context = {}
        self.student = student
        self.teacher = teacher
        self.practice = practice
        self.diary_days = diary_days
        self.file_name = '/generated_doc.docx'

    def create_docx(self):
        self.context.update(self.create_header(self.practice))
        self.context.update(self.create_teacher_info(self.teacher))
        self.context.update(self.create_user_info(self.student))
        self.context.update(self.create_body(self.diary_days))
        self.doc.render(self.context)
        self.doc.save(MEDIA_ROOT + self.file_name)

        return MEDIA_ROOT + self.file_name

    def create_header(self, practice):

        practice_data = {
            'practice_type': practice.practice_type,
            'date_start_day': practice.date_start.day,
            'date_start_month': practice.date_start.month,
            'date_start_year': practice.date_start.year,
            'date_end_day': practice.date_end.day,
            'date_end_month': practice.date_end.month,
            'date_end_year': practice.date_end.year,
            'practice_addres': practice.practice_addres,
        }

        return practice_data

    def create_user_info(self, student):
        user = {
            'user_full_name': student.full_name(),
            'user_group': student.group,
        }

        return user

    def create_teacher_info(self, teacher):
        teacher_data = {
            'teacher_short_name': teacher.short_name(),
            'teacher_position': teacher.position,
        }

        return teacher_data

    def create_body(self, diary_days):
        table_data = [
            {'date': day.date, 'work_info': day.work_info}
            for day in diary_days
        ]

        table = {
            'table' : table_data,
        }

        return table
