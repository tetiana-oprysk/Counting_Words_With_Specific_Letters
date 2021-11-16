from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import Length, DataRequired


class UploadVocabulary(FlaskForm):
    file = FileField(validators=[FileRequired()])
    submit = SubmitField(label='Confirm')


class AddNewWord(FlaskForm):
    add_new_word = StringField(label='Add new word...', validators=[Length(min=1, max=30)])
    submit = SubmitField(label='Submit')


class SearchWordsContainProvidedLetters(FlaskForm):
    letters = StringField(label='Write down your letters...', validators=[Length(min=1, max=30)])
    search = SubmitField(label='Search')
