import random


def mix_words(original_word):
    """
    перемешивает буквы в слове
    :return: mix_word
    """
    mix_word = list(original_word)  # превращаем строку в список
    random.shuffle(mix_word)  # миксуем буквы в слове, здесь слово является списком
    mix_word = ', '.join(mix_word)  # обратно превращаем список в строку
    mix_word = mix_word.replace(', ', '')  # удаляем из слова-строки ", "
    return mix_word
