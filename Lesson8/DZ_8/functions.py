import json
import random


def load_questions():
    """
    Загружает список вопросов из файла
    """
    with open("questions.json") as file:  # открыть файл на чтение
        all_questions_list = json.load(file)  # преобразовать в список
        return all_questions_list


def get_one_question(all_questions_list):
    """
    Возвращает один вопрос question_one из списка вопросов all_questions_list
    """
    question_one = random.choice(all_questions_list)  # рандомно выбираем 1 вопрос из всего списка
    all_questions_list.remove(question_one)  # удаляем этот вопрос из общего списка
    return question_one


def build_list(questions, question_one, user_answer, score):
    """
    создание списка questions
    """
    question_one['answer'] = user_answer  # добавляем в словарь новый ключ-значение
    question_one['score'] = score  # добавляем в словарь новый ключ-значение
    questions.append(question_one)  # добавляем в общий список наш вопрос с новым ключ-значением
    return questions


def statistic(questions):
    """
    Расчет статистики
    """
    sum_correct_answer = 0
    sum_score = 0
    for item in questions:
        if item["a"] == item["answer"]:  # если значение под ключом "а" равно зн-ию под ключом "answer"
            sum_correct_answer += 1  # счетчик правильных ответов
            sum_score += item["score"]  # счетчик суммарных баллов
    sum_answer = len(questions)
    print(f"Вот и все!\nОтвечено {sum_correct_answer} вопроса из {sum_answer}\nНабрано {sum_score} баллов")
