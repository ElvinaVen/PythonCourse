import requests
import random
#import BasicWord


def load_random_word():
    """
- получит список слов с внешнего ресурса,
- выберет случайное слово,
- создаст экземпляр класса `BasicWord`,
- вернет этот экземпляр.
    """
    response = requests.get("https://jsonkeeper.com/b/M1IA", verify=False)
    all_words_list = response.json()
    # print(all_words_list)
    random_word = get_random_word(all_words_list)
    #print(random_word)
    #print(random_word['word'], random_word['subwords'])
    list_random_word(random_word)
    original_word = random_word['word']
    subwords = random_word['subwords']
    #word = BasicWord.BasicWord(original_word, subwords)
    # print(word)
    return original_word, subwords


def get_random_word(all_words_list):
    """
    Возвращает один вопрос question_one из списка вопросов all_questions_list
    """
    random_word = random.choice(all_words_list)  # рандомно выбираем 1 вопрос из всего списка
    # all_words_list.remove(random_word)  # удаляем этот вопрос из общего списка
    return random_word


def list_random_word(random_word):
    """

    """

    original_word = random_word['word']
    subwords = random_word['subwords']

    # print(word)
    return original_word, subwords


def correct_word_len(uses_word):
    if len(uses_word) < 3:
        print("слишком короткое слово")