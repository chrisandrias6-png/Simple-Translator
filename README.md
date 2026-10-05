
Simple English-to-Arabic Translator 🌐

A simple English-to-Arabic dictionary translator built with Python and NumPy.

This is one of my first programming projects. The project uses two NumPy arrays: one containing English words and another containing their Arabic translations.

Features

- English-to-Arabic translation
- Simple word lookup
- Case-insensitive search
- Built with Python
- Uses NumPy

Example

Enter an English word: cat

Translation: قطة

Another example:

Enter an English word: New York

Translation: نيويورك

How it works

The program stores English words in one NumPy array and their corresponding Arabic translations in another array.

For example:

English       Arabic
-------------------------
cat      →    قطة
dog      →    كلب
AI       →    ذكاء اصطناعي

The program searches for the entered English word and returns the translation at the same position in the Arabic array.

Requirements

- Python 3
- NumPy

Install NumPy with:

pip install numpy

Run the project

Clone the repository:

git clone https://github.com/YOUR-USERNAME/Simple-Translator.git

Go into the project folder:

cd Simple-Translator

Run the program:

python translator.py

Current limitations

This is a simple dictionary-based translator, not a full machine translation model.

It currently contains a small number of words and phrases and does not understand the meaning or context of complete sentences.

Future improvements

- Add more words
- Support larger sentences
- Improve text processing
- Add more languages
- Add a graphical interface
- Experiment with machine learning
- Eventually build a neural-network-based translator

Technologies

- Python
- NumPy

Author

Created as a learning project while studying Python, NumPy, and Artificial Intelligence.
