import json


def load_students():
    """
    Загружает список студентов из файла
    """
    with open("students.json") as file: #  открыть файл на чтение
        #file = file.read()
        #print(file)
        file = json.load(file)
    return file

def load_professions():
    """
    Загружает список профессий из файла
    """
    with open("professions.json") as file: #  открыть файл на чтение
        #file = file.read()
        #print(file.read())
        file = json.load(file)
    #json.load(file)
    return file


def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    """
    file = load_students()

    for i in range(len(file)):
        if int(pk) == file[i]["pk"]:
            print(f"Студент {file[i]["full_name"]}")
            skills = ", ".join(file[i]["skills"])
            print(f"Знает {skills}")
            break
    else:
        print("У нас нет такого студента")
    student = file[i]["full_name"]
    return student

def get_profession_by_title(title):
    """
    Получает словарь с инфо о профе по названию
    """
    file = load_professions()

    for i in range(len(file)):
        if title == file[i]["title"]:

            break
    else:
        print("У нас нет такой специальности")
    profession = file[i]["title"]
    return profession

def check_fitness(student, profession):
    """
    которая получив студента и профессию, возвращала бы словарь типа:
    """
    #my_student = set(load_students())
    my_profession = set(load_professions())
    file = load_professions()
    my_profession = file[i]["skills"]
    print(student)