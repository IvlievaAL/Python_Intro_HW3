# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
N=int(input("Введите количество элементов в массиве: "))
if N<1:
    print ("Неправильно введены числа. N - натуральное число.")
else:
    import random
    OurArray=list()
    for i in range(N):
        OurArray.append(random.randrange(1,N+1))
    print (OurArray)
    X=int(input("Введите нужное Вам число: ")) # X == любое целое число
    IndexOfNumberMostCloseToX=0
    import math # считать будем абсолютную величину разности
    for i in range(len.OurArray):
        if math.abs(X)-OurArray[i]<math.abs(X)-OurArray[IndexOfNumberMostCloseToX]:
            IndexOfNumberMostCloseToX=i
    print(OurArray[IndexOfNumberMostCloseToX])