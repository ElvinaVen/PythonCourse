class Question:

    def __init__(self, question, difficulty_level, correct_answer, is_answer=False, user_answer=None):
        """
        Инициализирует
        """
        self.question = question
        self.difficulty_level = difficulty_level
        self.correct_answer = correct_answer
        self.is_answer = is_answer
        self.user_answer = user_answer
        self.score = 10 * int(self.difficulty_level)

    def get_points(self, user_question, user_answer):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        if user_question.is_correct(user_answer):
            return self.score

    def is_correct(self,user_answer):
        """Возвращает True, если ответ пользователя совпадает с верным ответов иначе False.
        """
        self.user_answer = user_answer
        if self.user_answer == self.correct_answer:
            return True

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        print(f"Вопрос: {self.question}\nСложность: {self.difficulty_level}/5")

    def build_positive_or_negative_feedback(self, user_question, user_answer):
        """Возвращает :
        Ответ верный, получено __ баллов. Ответ неверный, верный ответ __.
        """
        if user_question.is_correct(user_answer):
            print(f"Ответ верный, получено {user_question.get_points(user_question, user_answer)} баллов\n")
        else:
            print(f"Ответ неверный, верный ответ {self.correct_answer}\n")
