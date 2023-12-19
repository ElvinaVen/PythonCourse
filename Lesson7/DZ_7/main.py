import functions
import check_fitness

pk = input("Введите номер студента\n")
student = functions.get_student_by_pk(pk)  # вызов ф-ии получения словаря с данными студента по его pk

title = input(f"Выберите специальность для оценки студента {student}\n")
profession = functions.get_profession_by_title(title)

check_fitness.check_fitness(student, profession)
