class Player:

    def __init__(self, user_name, uses_words):
        """
        Инициализирует
        """
        self.user_name = user_name
        self.uses_words = uses_words

    def __repr__(self):
        return self.user_name, self.uses_words

    def get_count_uses_words(self):
        """
        получение количества использованных слов (возвращает int)
        """
        pass

    def add_word_in_uses_words(self, uses_word, uses_words_list):
        """
        добавление слова в использованные слова (ничего не возвращает)
        """

        uses_words_list.append(uses_word)
        print(uses_words_list)


    def correct_uses_word(self):
        """
        проверка использования данного слова до этого (возвращает bool)
        """
        pass
