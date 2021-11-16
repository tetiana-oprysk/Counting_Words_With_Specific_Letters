import re
from collections import Counter


def upload_vocabulary(file_path) -> list:
    with open(file_path, encoding='utf-8') as file:
        vocabulary_file = file.read()
        vocabulary = re.findall(r"[a-zA-Z'`-]+", vocabulary_file)

    return vocabulary


def add_word_to_vocabulary(vocabulary: list) -> list:
    new_word = str(input('Write down new word: '))
    vocabulary.append(new_word)

    return vocabulary


def words_that_contain_provided_letters(vocabulary, pattern) -> list:

    def is_sublist(pattern, word) -> bool:
        pattern_counter = Counter(pattern)
        word_counter = Counter(word)

        for item, count in pattern_counter.items():
            if count > word_counter[item]:
                return False

        return True

    words_with_provided_letters = [word for word in vocabulary if is_sublist(list(pattern.lower()), list(word.lower()))]
    return words_with_provided_letters


def find_number_of_words_that_contain_provided_letters(vocabulary, pattern) -> int:
    return len(words_that_contain_provided_letters(vocabulary, pattern))


if __name__ == '__main__':
    # Upload vocabulary by file path
    file_path = input('File path (only txt): ')
    vocabulary = upload_vocabulary(file_path)

    # Ability to add a new word to the dictionary
    while True:
        add_new_word = str(input('Would you like to add new word? (y/n): '))
        if add_new_word == 'y':
            vocabulary = add_word_to_vocabulary(vocabulary)
            print(f'Your updated vocabulary:\n{vocabulary}')
        else:
            print(f'\nYour vocabulary:\n{vocabulary}')
            break

    # test_vocabulary = ['By', 'default', 'the', 'value', 'will', 'be', 'the', 'filename', 'sent', 'data', 'word']

    # Write down letters to search words which contain that letters
    pattern = str(input('\nWrite down your letters: ')).lower()
    words = words_that_contain_provided_letters(vocabulary, pattern)
    print('Number of words that contain provided letters: ',
          find_number_of_words_that_contain_provided_letters(vocabulary, pattern))

    # Print only first ten words in list
    print('Your words: ', ', '.join(words))
