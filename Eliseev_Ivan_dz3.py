'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
'''

library = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(name):
    if name[0] == name[0].upper():
        name = name.lower()
        print(name.capitalize())
    else:
        print(library.get(name))

num_translate('Two')

"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}
"""

def thesaurus(*names):
    to_dict = dict()
    for el in names:
        to_dict.setdefault(el[0], [])
        to_dict[el[0]].append(el)
    return to_dict

print(thesaurus('Ivan', 'Maria', 'Nick'))

"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    joke_list = []
    for i in range(num):
        word_1 = random.choice(nouns)
        word_2 = random.choice(adverbs)
        word_3 = random.choice(adjectives)
        joke_list.append(f'{word_1} {word_2} {word_3}')
    return joke_list

print(get_jokes(2))

#

