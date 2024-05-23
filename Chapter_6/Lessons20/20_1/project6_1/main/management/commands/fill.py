from django.core.management import BaseCommand
from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Semenov', 'first_name': 'Semen'},
            {'last_name': 'Alexandrov', 'first_name': 'Alex'},
            {'last_name': 'Sidorov', 'first_name': 'Sidr'},
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
        ]
        # for item in student_list:
        #     Student.objects.create(**item)
        students_for_create = []
        for item in student_list:
            students_for_create.append(Student(**item))
        Student.objects.bulk_create(students_for_create)
