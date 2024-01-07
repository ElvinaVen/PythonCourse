class BasicWord:

    def __init__(self, original_word, subwords):
        """
        Инициализирует
        """
        self.original_word = original_word
        self.subwords = subwords

    def __repr__(self):
        return self.original_word, self.subwords

    def correct_word(self, uses_word, subwords):
        """
        проверку введенного слова в списке допустимых подслов (вернет bool)
        """
        if uses_word in subwords:
            print("все ок")
        else:
            print("неверно")

    def get_count_subwords(self):
        """подсчет количества подслов (вернет int)"""
        pass
