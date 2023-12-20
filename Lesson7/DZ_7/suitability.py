import functions


def check_fitness(student, profession):
    """
    получив студента и профессию, показывает его пригодность
    """
    file_prof = functions.load_professions()  # вызов функции загрузки списка профессий из файла
    file_stud = functions.load_students()  # вызов функции загрузки списка студентов из файла

    for prof_dict in file_prof:
        if profession == prof_dict["title"]:
            need_skill = prof_dict["skills"]  # вывод списка необходимых навыков для опред-ой профессии

    for stud_dict in file_stud:
        if student == stud_dict["full_name"]:
            student_skill = stud_dict["skills"]  # вывод списка навыков, которые есть у студента
            yes_skill = set(student_skill).intersection(need_skill)  # вывод необходимых навыков, которые есть у
            # студента
    not_skill = set(need_skill).difference(student_skill)  # вывод навык, которых недостает студенту
    percent = (len(yes_skill) / len(need_skill)) * 100  # счет процента пригодности

    fitness = {
        "has": list(yes_skill),
        "lacks": list(not_skill),
        "percent": percent
    }

    return fitness
