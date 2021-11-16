# Counting Words With Specific Letters

In that repository you can find **main_program.py** file, which contain program for counting words that includes specific letters. Using this program you can:
 - Upload vocabulary by file path (you must use files only in .txt format, but the words in this dictionary can be separated somehow - semicolon, comma, newline etc.)
 - Add new word to your vocabulary
 - Find exact number of words that contain provided letters (a word contain all writed down letters)
 - Show words that contain provided letters

But I thought it would be more interesting to design this program in the form of REST API, so in this repository you can also find the ***app*** I developed too :)

This ***app*** have the same functionality and capabilities as the **main_program.py**, but I configured a client-side server architecture here.


## Example:
Your vocabulary: `['By', 'default', 'the', 'value', 'will', 'be', 'the', 'filename', 'sent', 'data', 'word']` 

And you want to find words with the following letters: "aeu"
So you get the following answer:
| letters |number of words|     words    | 
|---------|---------------|--------------|
|   aeu   |       2       |default, value|

The table will show only the first 10 words that contain specific letters.