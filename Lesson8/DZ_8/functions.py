#from main import Question
import json
import random

def create_list(question_one):
    question = question_one["q"]
    hard = question_one['d']
    correct_answer = question_one['a']
    return question, hard, correct_answer

def get_difficulty_level(user_question):
    difficulty_level = user_question.build_question()[1]
    print(f"Сложность: {difficulty_level}/5")


def get_question(user_question):
    question = user_question.build_question()[0]
    print(f"Вопрос: {question}")



def load_questions():
    """
    Загружает список вопросов из файла
    """
    with open("questions.json") as file:  # открыть файл на чтение
        all_questions = json.load(file)
        return all_questions

def get_questions(all_questions):
    """
    Получает словарь с инфо о профе по названию
    """
    question_one = random.choice(all_questions)  # выбирает 1
    all_questions.remove(question_one)
    return question_one

