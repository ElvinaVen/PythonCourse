import json
import random


class Question:
    all_questions = []
    sum_correct_answer = []
    sum_balls = 0
    sum_user_answer = []

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

        if user_question.is_correct(user_answer):
            ball = 10 * int(self.hard)
            return ball

    def is_correct(self, user_answer):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """

        self.user_answer = user_answer
        if self.user_answer == self.correct_answer:
            return True

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
        Question.sum_user_answer.append("True")
        if user_question.is_correct(user_answer):
            Question.sum_correct_answer.append("True")
            Question.sum_balls += user_question.get_points()
            text = f"Ответ верный, получено {user_question.get_points()} баллов\n"
        else:
            text = f"Ответ неверный, верный ответ {self.correct_answer}\n"

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
        Question.all_questions = json.load(file)
    return


def get_questions():
    """
    Получает словарь с инфо о профе по названию
    """
    a = len(Question.all_questions)
    question_index = random.randint(0, a - 1)
    question_one = Question.all_questions[question_index]
    del_questions(question_index)
    return question_one


def del_questions(question_index):
    Question.all_questions.remove(Question.all_questions[question_index])


def statistic():
    sum_correct_answer = len(Question.sum_correct_answer)
    sum_balls = Question.sum_balls
    sum_answer = len(Question.sum_user_answer)
    return sum_correct_answer, sum_answer, sum_balls


def test(question_one):
    question = question_one["q"]
    hard = question_one['d']
    correct_answer = question_one['a']
    return question, hard, correct_answer


load_questions()
print("Игра начинается!")
while len(Question.all_questions) != 0:
    question_one = get_questions()
    question, hard, correct_answer = test(question_one)
    user_question = Question(question, hard, correct_answer)
    print(f"Вопрос: {get_question()}")
    print(f"Сложность: {get_hard()}/5")
    user_answer = input()
    user_question.is_correct(user_answer)
    user_question.get_points()
    print(user_question.build_positive_or_negative_feedback())

sum_correct_answer, sum_answer, sum_balls = statistic()
print(f"Вот и все!\nОтвечено {sum_correct_answer} вопроса из {sum_answer}\nНабрано {sum_balls} баллов")
