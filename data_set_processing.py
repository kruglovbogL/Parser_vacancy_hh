from multiprocessing import cpu_count

import gensim.downloader as api  # installed scipy-1.12.0
from gensim.models.word2vec import Word2Vec

dataset = api.load("text8")  # загрузка набора данных "text8"
#
data = []  # извлечь список слов из датасета
for word in dataset:
    data.append(word)
#
# Разделим данные на две части
data_1 = data[:1200]  # используется для обучения модели
data_2 = data[1200:]  # используется для обновления модели
#
# Обучение модели Word2Vec
w2v_model = Word2Vec(data_1, min_count=0, workers=cpu_count())
#
print(w2v_model.wv[word])  # вектор слов для слова "время"

def input_word(word):
    words = input()
