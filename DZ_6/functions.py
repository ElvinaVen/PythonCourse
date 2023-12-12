import random


def read_file():
    """
    чтение из файла, загрузка оригинальных слов
    :return:
    """
    original_word = []
    file = open('words.txt')  # считываем построчно слова из файла
    for word in file:
        original_word.append(word.strip())

    file.close()
    return original_word



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


def player_list(user_name, score):
    """
    записывает имя игрока и количество набранных баллов в файл
    :param score: user_name, score
    :return:
    """
    with open('history.txt', 'a') as file:  # добавляет в конец файла новую строчку по новому игроку
        file.write(f"{user_name} {score}\n")
    print("Ответы записаны")

def history_read():
    """

    """
    players_list = []
    players_ball_list = []
    with open('history.txt', 'r') as file:  # открываем на чтение файл история или пайтон сам его создаст
        for player in file:  # передвигаемся по строчкам-игрокам
            player, ball = player.strip().split(' ')  # присваиваем переменным игрок и балл значения
            players_ball_list.append(ball.strip())
            players_list.append(player.strip())
    return players_list, players_ball_list


def statistic(players_list, players_ball_list):
    """
показывает лидера и общее количество игр
    :return:
    """
    lider = max(players_ball_list)  # задаем переменной лидер минимальное значение 0
    player = len(players_list)
    print(f'Всего игр сыграно: {player} \nМаксимальный рекорд: {lider}')
