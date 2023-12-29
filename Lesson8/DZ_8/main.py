from functions import load_questions, get_one_question, statistic, build_list
from Classes import Question

questions = []
all_questions_list = load_questions()  # вызов ф-ии выгрузки списка вопросов из файла
print("Игра начинается!!!")
while len(all_questions_list) != 0:
    question_one = get_one_question(all_questions_list)  # вызов ф-ии возврата одного вопрос question_one из списка
                                                         # вопросов all_questions_list
    user_question = Question(question_one["q"], question_one['d'], question_one['a'])  # создаем экземпляр класса,
                                                         # в который передаем вопрос, сложность и прав. ответ
    user_question.build_question()  # Вызов ф-ии возврата вопроса и сложности для юзера
    user_answer = input("Ваш ответ: ")
    score = user_question.get_points()  # Вызов ф-ии возврата кол-ва баллов
    user_question.build_positive_or_negative_feedback()  # вызов ф-ии build_positive_or_negative_feedback
    questions = build_list(questions, question_one, user_answer, score)  # вызов ф-ии создания списка questions
statistic(questions)  # Вызов ф-ии расчета статистики
