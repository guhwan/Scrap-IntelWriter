import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

from scripts import scraper


articles = [
    'snake',
    'cat'
]

# tokenizer-master
tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(articles)
word_index = tokenizer.word_index
print(word_index)

# create basic word / phrase processor..
#entry = scraper.list_categories("potato")
#print(entry)




























