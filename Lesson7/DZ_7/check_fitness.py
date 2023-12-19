import functions


def check_fitness(student, profession):
    """
    получив студента и профессию, возвращала бы словарь типа:
    """
    file_prof = functions.load_professions()
    file_stud = functions.load_students()

    for i in range(len(file_prof)):
        if profession == file_prof[i]["title"]:
            need_skill = file_prof[i]["skills"]  # "skills": ["Python", "Linux", "Docker", "SQL", "Flask"]

    for i in range(len(file_stud)):
        if student == file_stud[i]["full_name"]:
            student_skill = file_stud[i]["skills"]
            yes_skill = set(student_skill).intersection(need_skill)

    not_skill = set(need_skill).difference(student_skill)
    print(f"Пригодность {(len(yes_skill) / len(need_skill)) * 100}%")
    print(f"{student} знает {", ".join(yes_skill)}")  # "skills": ["Python", "Go", "Linux"]
    print(f"{student} не знает {", ".join(not_skill)}")
