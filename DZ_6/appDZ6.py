import random


def mix_words():
    score = 0
    with open('words.txt', 'r') as file:  # считываем построчно слова из файла
        for word in file:
            word = word.strip()  # убираем символ переноса на строку из слова
            mix_word = list(word.strip())  # превращаем строку в список и удаляем символ переноса на строку
            random.shuffle(mix_word)
            mix_word = ', '.join(mix_word)  # превращаем список в строку
            mix_word = mix_word.replace(', ', '')  # удаляем из строки ", "

            user_answer = input(f'Угадайте слово: {mix_word}\n')
            if user_answer == word:
                print('Верно! Вы получаете 10 очков.')
                score += 10
            else:
                print(f'Неверно! Верный ответ – {word}.')
    return score


def player_statistic(score):
    with open('history.txt', 'a') as file:
        file.write(f"{user_name} {score}\n")
    print("Ответы записаны")


def statistic():
    lider = 0
    index = 0
    with open('history.txt', 'r') as file:
        for line in file:
            player, ball = line.strip().split(' ')
            index += 1
            if int(ball) > int(lider):
                lider = ball
    print(f'Всего игр сыграно: {index} \nМаксимальный рекорд: {lider}')


user_name = input('Введите ваше имя:\n')
answers_sum = mix_words()
player_statistic(answers_sum)
statistic()
