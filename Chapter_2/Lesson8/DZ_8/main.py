import json
import random

class Question:
    def __init__(self, question, hard, correct_answer, isanswer=False, user_answer=None):
        """
        Инициализирует
        """
        self.question = question
        self.hard = hard
        self.correct_answer = correct_answer
        self.isanswer = isanswer
        self.user_answer = user_answer


    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        if user_question.is_correct(user_answer) == True:
            ball = 10 * int(self.hard)
            return ball

    def is_correct(self, user_answer):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        self.user_answer = user_answer
        if self.user_answer == self.correct_answer:
            return True
            #print("True")
        else:
            False
            #print("False")



    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return self.question, self.hard

    def build_positive_or_negative_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ __
        """

        if user_question.is_correct(user_answer) == True:

            text = f"Ответ верный, получено {user_question.get_points()} баллов"
        else:
            text = f"Ответ неверный, верный ответ {self.correct_answer}"

        return text
def get_hard():
    question, hard = user_question.build_question()
    return hard

def get_question():
    question, hard = user_question.build_question()
    return question

def load_questions():
    """
    Загружает список вопросов из файла
    """
    with open("questions.json") as file:  # открыть файл на чтение
        question = json.load(file)
    return question


def get_questions():
    """
    Получает словарь с инфо о профе по названию
    """
    file = load_questions()  # вызов функции загрузки списка профессий из файла

    for question in file:  # перебор списка в файле профессий
        questions.append(question)
    return random.sample(questions,1)


questions = []
get_questions()


question_1 = get_questions()
#print(question_1)
def test(question_1):
    for line in question_1:
        question = line["q"]
        hard = line['d']
        correct_answer = line['a']
        return question, hard, correct_answer
#question_1 = Question()
question, hard, correct_answer = test(question_1)
#print(testik)

user_question = Question(question, hard, correct_answer)

print("Игра начинается!")
i = 0
for i in range(len(question)):

    print(f"Вопрос: {get_question()}")
    print(f"Сложность: {get_hard()}/5")
    user_answer = input()
    user_question.is_correct(user_answer)
    user_question.get_points()
    print(user_question.build_positive_or_negative_feedback())
    i += 1
