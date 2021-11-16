from app import app
import re


class FileService:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_and_create_vocabulary(self) -> list:
        """
        :return: vocabulary list which contain all words from specified file
        """
        with open(self.file_path, encoding='utf-8') as f:
            vocabulary_file = f.read()
            vocabulary = re.findall(r"[a-zA-Z.'`-]+", vocabulary_file)
        return vocabulary

    def update_vocabulary(self, new_word):
        """
        Updated file with vocabulary
        :param new_word: str() type
        :return: None
        """
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(f', {new_word}')
