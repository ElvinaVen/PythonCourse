import functions
import suitability

pk = input("Введите номер студента\n")
student = functions.get_student_by_pk(pk)  # вызов ф-ии получения словаря с данными студента по его pk
title = (input(f"Выберите специальность для оценки студента {student}\n")).title()  # вводим нужную проф-ию, первую
# букву делаем заглавной
profession = functions.get_profession_by_title(title)  # вызов функции получения словаря с инфо о профе по названию
fitness = suitability.check_fitness(student, profession)  # вызов функции пригодности по опр-му
# студенту и профессии

print(f"Пригодность {fitness["percent"]}%")

if fitness["percent"] == 100:
    print(f"Студент знает всё!")
elif fitness["percent"] == 0:
    print(f"Студент не компетентен для данной профессии")
elif 0 < fitness["percent"] < 100:
    print(f"{student} знает {", ".join(fitness["has"])}")
    print(f"{student} не знает {", ".join(fitness["lacks"])}")
