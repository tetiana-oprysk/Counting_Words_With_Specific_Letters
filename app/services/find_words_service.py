from collections import Counter


class FindWords:
    def __init__(self, vocabulary, pattern):
        self.vocabulary = vocabulary
        self.pattern = pattern

    def words_that_contain_provided_letters(self) -> list:
        """
        :return: list of found words which contain provided letters
        """
        words_with_provided_letters = [word for word in self.vocabulary if
                                       self.is_sublist(list(self.pattern.lower()), list(word.lower()))]
        return words_with_provided_letters

    def find_number_of_words_that_contain_provided_letters(self) -> int:
        """
        :return: number of found words which contain provided letters
        """
        return len(self.words_that_contain_provided_letters())

    @staticmethod
    def is_sublist(pattern, word) -> bool:
        pattern_counter = Counter(pattern)
        word_counter = Counter(word)

        for item, count in pattern_counter.items():
            if count > word_counter[item]:
                return False

        return True
