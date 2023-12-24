#from main import user_question
#from main import user_answer


class Question:
    all_questions = []
    sum_correct_answer = []
    sum_balls = 0
    sum_user_answer = []

    def __init__(self, question, hard, correct_answer, is_answer=False, user_answer=None):
        """
        Инициализирует
        """
        self.question = question
        self.hard = hard
        self.correct_answer = correct_answer
        self.is_answer = is_answer
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
