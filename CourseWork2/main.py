import utils
import Player
import BasicWord

original_word, subwords = utils.load_random_word()
user_name = input("Введите имя игрока:\n")
player = Player.Player(user_name, original_word)
word = BasicWord.BasicWord(original_word, subwords)
print(f"Привет, {user_name}!")
print(f"Составьте {len(subwords)} слов из слова {str(original_word).upper()}")
print(f"Слова должны быть не короче 3 букв\nЧтобы закончить игру, угадайте все слова или напишите 'stop'"
      f"\nПоехали, ваше первое слово?")
uses_words_list = []
while len(uses_words_list) != len(subwords):
    uses_word = input()
    utils.correct_word_len(uses_word)
    word.correct_word(uses_word, subwords)
    player.add_word_in_uses_words(uses_word, uses_words_list)
print("Игра завершена, вы угадали 8 слов!")

