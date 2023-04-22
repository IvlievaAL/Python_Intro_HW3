# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную 
# ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо 
# только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# Метод определит, есть ли во введенном слове кириллица.
# Если да, то вернет кириллическую таблицу стоимости, нет - латиницу.
def is_our_word_cyrillic(our_word, points_cyril, points_latin):
    kirillitsa = ("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    is_our_word_cyrillic_char = [char for char in kirillitsa if char in our_word]
    if is_our_word_cyrillic_char:
        points = points_cyril
    else:
        points = points_latin
    return points

# Метод вернет список очков за каждую букву слова.
def our_word_costs_per_char(our_word, our_points):
    costs_of_our_word_per_char = []
    for char in our_word:
        for key, value in our_points.items():
            if char in value:
                costs_of_our_word_per_char.append(key)
    return costs_of_our_word_per_char
                
our_word = input("Введите слово на русском или на английском: ").upper()
points_cyril = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
points_latin = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
our_points = is_our_word_cyrillic(our_word, points_cyril, points_latin)
costs_of_our_word = our_word_costs_per_char(our_word, our_points)
print(sum(costs_of_our_word))