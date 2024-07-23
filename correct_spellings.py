# -*- coding: utf-8 -*-
"""correct spellings.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xRkQllo_IkQVjRHfJY7IL4cpn-GToof5
"""

from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a Word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)

pip install pyspellchecker