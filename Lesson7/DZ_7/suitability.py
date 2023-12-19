import functions


def check_fitness(student, profession):
    """
    получив студента и профессию, показывает его пригодность
    """
    file_prof = functions.load_professions()  # вызов функции загрузки списка профессий из файла
    file_stud = functions.load_students()  # вызов функции загрузки списка студентов из файла

    for i in range(len(file_prof)):
        if profession == file_prof[i]["title"]:
            need_skill = file_prof[i]["skills"]  # вывод списка необходимых навыков для опред-ой профессии

    for i in range(len(file_stud)):
        if student == file_stud[i]["full_name"]:
            student_skill = file_stud[i]["skills"]  # вывод списка навыков, которые есть у студента
            yes_skill = set(student_skill).intersection(need_skill)  # вывод необходимых навыков, которые есть у
                                                                     # студента

    not_skill = set(need_skill).difference(student_skill)  # вывод навык, которых недостает студенту
    print(f"Пригодность {(len(yes_skill) / len(need_skill)) * 100}%")  #  счет процента пригодности
    print(f"{student} знает {", ".join(yes_skill)}")
    print(f"{student} не знает {", ".join(not_skill)}")
