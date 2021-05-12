import urllib.request

import numpy as np

# отправляем в переменную всё содержимое текстового файла

# Считываем файл c сочинениями Чехова по http (Вариант 1)
with urllib.request.urlopen('https://thecode.media/wp-content/uploads/2021/04/che-1.txt') as f:
    text = f.read().decode('utf-8')

# Или локально (Вариант 2)
# text = open('che.txt', encoding='utf-8').read()

# разбиваем текст на отдельные слова (знаки препинания останутся рядом со своими словами)
corpus = text.split()


# делаем новую функцию-генератор, которая определит пары слов
def make_pairs(corpus):
    # перебираем все слова в корпусе, кроме последнего
    for i in range(len(corpus) - 1):
        # генерируем новую пару и возвращаем её как результат работы функции
        yield (corpus[i], corpus[i + 1])

# вызываем генератор и получаем все пары слов
pairs = make_pairs(corpus)

word_dict = {}

# перебираем все слова попарно из нашего списка пар
for word_1, word_2 in pairs:
    # если первое слово уже есть в словаре
    if word_1 in word_dict.keys():
        # то добавляем второе слово как возможное продолжение первого
        word_dict[word_1].append(word_2)
    # если же первого слова у нас в словаре не было
    else:
        # создаём новую запись в словаре и указываем второе слово как продолжение первого
        word_dict[word_1] = [word_2]

# случайно выбираем первое слово для старта
first_word = np.random.choice(corpus)

# если в нашем первом слове нет больших букв
while first_word[0].islower():
    # то выбираем новое слово случайным образом
    # и так до тех пор, пока не найдём слово с большой буквой
    first_word = np.random.choice(corpus)

# делаем наше первое слово первым звеном
chain = [first_word]

# сколько слов будет в готовом тексте
n_words = 100

# делаем цикл с нашим количеством слов
for i in range(n_words):
    # на каждом шаге добавляем следующее слово из словаря, выбирая его случайным образом из доступных вариантов
    chain.append(np.random.choice(word_dict[chain[-1]]))

# выводим результат
print(' '.join(chain))
