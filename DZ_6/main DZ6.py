import functions

user_name = input('Введите ваше имя:\n')

original_words = functions.read_file()

i=0
while i < len(original_words):
    mix_word = functions.mix_words(original_words[i])  # запускаем функцию перемешивания букв в слове и результат помещаем в answers_sum

    user_answer = input(f'Угадайте слово: {mix_word}\n')  # предлагаем угадать слово

    score = 0  # задаем количесвто баллов

    if user_answer == original_words[i]:  # если ответ пользователя равен слову
        print('Верно! Вы получаете 10 очков.')
        score += 10  # добавляем 10 баллов молодцу
    else:
        print(f'Неверно! Верный ответ – {original_words[i]}.')
    i += 1

functions.player_list(user_name, score)  # запускаем функцию записи имени игрока и его баллов
player, ball = functions.history_read()

functions.statistic(player, ball)  # запускаем функцию по статистике
