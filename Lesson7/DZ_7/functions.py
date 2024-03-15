import json


def load_students():
    """
    Загружает список студентов из файла
    """
    with open("students.json") as file:  # открыть файл на чтение
        data_stud = json.load(file)  # переделываем джейсон файл в пайтон словарь
    return data_stud


def load_professions():
    """
    Загружает список профессий из файла
    """
    with open("professions.json") as file:  # открыть файл на чтение
        data_prof = json.load(file)
    return data_prof


def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    """
    file = load_students()  # вызов функции загрузки списка студентов из файла

    for stud_dict in file:  # перебор списка в файле студентов
        if stud_dict["pk"] == int(pk):
            print(f"Студент {stud_dict["full_name"]}")
            skills = ", ".join(stud_dict["skills"])  # список превращаем в строку
            print(f"Знает {skills}")
            break
    else:
        print("У нас нет такого студента")
        quit()  # выход из программы
    student = stud_dict["full_name"]  # присваиваем студенту его имя по порядковому номеру рк
    return student


def get_profession_by_title(title):
    """
    Получает словарь с инфо о профе по названию
    """
    file = load_professions()  # вызов функции загрузки списка профессий из файла

    for prof_dict in file:  # перебор списка в файле профессий
        if title == prof_dict["title"]:
            profession = prof_dict["title"]
            break
    else:
        print("У нас нет такой специальности")
        quit()
    return profession
