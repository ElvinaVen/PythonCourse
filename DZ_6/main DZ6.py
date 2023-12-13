import functions
import randomizer

user_name = input('Введите ваше имя:\n')

original_words = functions.read_file()

i = 0
score = 0  # задаем количество баллов

while i < len(original_words):
    mix_word = randomizer.mix_words(original_words[i])  # запускаем функцию перемешивания букв в слове
    user_answer = input(f'Угадайте слово: {mix_word}\n')  # предлагаем угадать слово

    if user_answer == original_words[i]:  # если ответ пользователя равен слову
        print('Верно! Вы получаете 10 очков.')
        score += 10  # добавляем 10 баллов молодцу
    else:
        print(f'Неверно! Верный ответ – {original_words[i]}.')
    i += 1

functions.write_plays_list(user_name, score)  # запускаем функцию записи имени игрока и его баллов
players_list, players_score_list = functions.history_read()  # запускаем функцию чтения из файла истории игроков и балов
functions.statistic(players_list, players_score_list)  # запускаем функцию по статистике
