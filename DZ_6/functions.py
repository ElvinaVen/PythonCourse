import random


def mix_words(original_word):
    """
    перемешивает буквы в слове
    :return: количество баллов score
    """
    # score = 0  # задаем количесвто баллов
    # with open('words.txt') as file:  # считываем построчно слова из файла
    # for word in file:  # передвигаемся по словам
    # original_word = original_word.strip()  # убираем из слова символ переноса на строку
    mix_word = list(original_word)  # превращаем строку в список
    random.shuffle(mix_word)  # миксуем буквы в слове, здесь слово является списком
    mix_word = ', '.join(mix_word)  # обратно превращаем список в строку
    mix_word = mix_word.replace(', ', '')  # удаляем из слова-строки ", "
    return mix_word


def read_file():
    """
    чтение из файла
    :return:
    """
    file = open('words.txt')  # считываем построчно слова из файла
    for original_word in file:
        # print(original_word)
        return original_word.strip()
    file.close()
    # return original_word


def statistic():
    """
показывает лидера и общее количество игр
    :return:
    """
    lider = 0  # задаем переменной лидер минимальное значение 0
    plays_sum = 0  # здесь будем считать общее количество игр
    with open('history.txt', 'r') as file:  # открываем на чтение файл история или пайтон сам его создаст
        for player in file:  # передвигаемся по строчкам-игрокам
            player, ball = player.strip().split(' ')  # присваиваем переменным игрок и балл значения из строки, которые разделены пробелом
            plays_sum += 1  # счетчик количества игр
            if int(ball) > int(lider):  # если балл больше минимального
                lider = ball  # присваиваем лидерному баллу новый балл
    print(f'Всего игр сыграно: {plays_sum} \nМаксимальный рекорд: {lider}')


def player_list(user_name, score):
    """
    записывает имя игрока и количество набранных баллов в файл
    :param score: user_name, score
    :return:
    """
    with open('history.txt', 'a') as file:  # добавляет в конец файла новую строчку по новому игроку
        file.write(f"{user_name} {score}\n")
    print("Ответы записаны")
