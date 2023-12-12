import functions

user_name = input('Введите ваше имя:\n')
original_word = functions.read_file()

# original_word = read_file()

# from functions import mix_words

mix_word = functions.mix_words(original_word)  # запускаем функцию перемешивания букв в слове и результат помещаем в answers_sum

user_answer = input(f'Угадайте слово: {mix_word}\n')  # предлагаем угадать слово

# from question import questions_list
# questions_list(user_answer)
score = 0  # задаем количесвто баллов
if user_answer == original_word:  # если ответ пользователя равен слову
    print('Верно! Вы получаете 10 очков.')
    score += 10  # доббавляем 10 баллов молодцу
else:
    print(f'Неверно! Верный ответ – {original_word}.')

functions.player_list(user_name, score)  # запускаем функцию записи имени игрока и его баллов

functions.statistic()  # запускаем функцию по статистике
