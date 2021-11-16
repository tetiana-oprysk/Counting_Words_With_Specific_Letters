import os
import re
from collections import Counter
from app import app
from app.services.file_service import FileService
from app.services.find_words_service import FindWords
from app.forms import UploadVocabulary, AddNewWord, SearchWordsContainProvidedLetters
from flask import render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = UploadVocabulary()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('vocabulary', filename=filename))

    return render_template('form_to_upload_vocabulary.html', form=form)


# def words_that_contain_provided_letters(vocabulary, pattern) -> list:
#
#     def is_sublist(pattern, word) -> bool:
#         pattern_counter = Counter(pattern)
#         word_counter = Counter(word)
#
#         for item, count in pattern_counter.items():
#             if count > word_counter[item]:
#                 return False
#
#         return True
#
#     words_with_provided_letters = [word for word in vocabulary if is_sublist(list(pattern.lower()), list(word.lower()))]
#     return words_with_provided_letters
#
#
# def find_number_of_words_that_contain_provided_letters(vocabulary, pattern) -> int:
#     return len(words_that_contain_provided_letters(vocabulary, pattern))


@app.route('/vocabulary', methods=['GET', 'POST'])
def vocabulary():
    # Search file with vocabulary
    file = request.args.get('filename', None)
    file_path = f"{app.config['UPLOAD_FOLDER']}\\{file}"

    # Upload file with vocabulary
    file_service = FileService(file_path)
    vocabulary = file_service.read_file_and_create_vocabulary()

    # Form for adding new word to vocabulary
    form_add_new_word = AddNewWord()
    if form_add_new_word.validate_on_submit():
        new_word = request.form['add_new_word']
        file_service.update_vocabulary(new_word)
        flash('New word successfully added!')
        return redirect(url_for('vocabulary', filename=file))

    # Form for searching words
    form_search_words_contain_provided_letters = SearchWordsContainProvidedLetters()

    global number_of_words, words, letters
    number_of_words = None
    words_str = None
    letters = None

    if form_search_words_contain_provided_letters.validate_on_submit():
        letters = request.form['letters']

        find_words = FindWords(vocabulary, letters)
        number_of_words = find_words.find_number_of_words_that_contain_provided_letters()
        words = find_words.words_that_contain_provided_letters()
        words_str = ', '.join(words[:10])

    vocabulary_str = ', '.join(vocabulary)
    return render_template('vocabulary.html',
                           form_add_new_word=form_add_new_word,
                           form_search=form_search_words_contain_provided_letters,
                           vocabulary=vocabulary,
                           vocabulary_str=vocabulary_str,
                           number_of_words=number_of_words,
                           words=words_str,
                           letters=letters)
