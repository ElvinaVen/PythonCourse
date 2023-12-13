WORDS_SOURCE = "words.txt"
HISTORY_FILE = "history.txt"


def read_file():
    """
    чтение из файла, загрузка оригинальных слов
    :return: original_word
    """
    original_word = []
    with open(WORDS_SOURCE) as file:
        for word in file:
            original_word.append(word.strip())
        return original_word


def write_plays_list(user_name, score):
    """
    записывает имя игрока и количество набранных баллов в файл
    """
    with open(HISTORY_FILE, 'a') as file:  # добавляет в конец файла новую строчку по новому игроку
        file.write(f"{user_name} {score}\n")
    print("Ответы записаны")


def history_read():
    """
    чтение из файла
    """
    players_list = []
    players_score_list = []
    with open(HISTORY_FILE, 'r') as file:  # открываем на чтение файл история
        for line in file:  # передвигаемся по строчкам-игрокам
            player, score = line.strip().split(' ')  # присваиваем переменным игрок и score значения
            players_score_list.append(score.strip())
            players_list.append(player.strip())
    return players_list, players_score_list


def statistic(players_list, players_score_list):
    """
    показывает лидера и общее количество игр
    :return:
    """
    lider = max(players_score_list)
    players_count = len(players_list)
    print(f'Всего игр сыграно: {players_count} \nМаксимальный рекорд: {lider}')
