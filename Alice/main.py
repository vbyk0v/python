# -*- coding: utf8 -*-
import time


def words_count(timer=True):  # обьявление функции в которой будет преобразован файл в текст,
    # таймер для вывода времени выполнения
    start = time.time()  # начало таймера
    a_string = ''  # создание пустой строки
    with open('alice.txt', encoding='utf-8-sig') as txt:  # открыть текстовый файл в кодировке utf-8
        for line in txt:  # перебор строк в открытом файле
            a_string = a_string + str(line)  # в пустую строку приплюсовывать все строки из файла

    string_filter = str.maketrans(dict.fromkeys(".,!;:'’‘)(?"))  # создание фильтра специальных символов
    b_string = a_string.translate(string_filter)  # применение фильтра к строке
    c_string = b_string.lower()  # преобразование всех прописных букв в строчные
    d_string = c_string.replace("-", " ")  # замена тире на пробел
    #  print(d_string)  # вывод отформатированного текста

    words = d_string.split()  # создание из строки списка где каждое слово является элементом списка
    #  print(words) вывод списка
    alice_dict = dict()  # создать пустой словарь (ключ: значение), ключем будет слово, значение число слов

    for word in words:  # для каждого элемента списка (слова) перебор
        if word in alice_dict:  # если слово содержится в списке ключей
            alice_dict[word] += 1  # то значение экого ключа увеличивается на один
        else:
            alice_dict[word] = 1  # а если ключа нет, то создать ключ и присвоить значение 1
    # print(counts)  вывод заполненного знгачениями словаря

    with open('out.txt', 'w') as f:  # открыть новый файл для редактирования
        for key, value in alice_dict.items():  # для ключа и значения в словаре
            print(key, ":", value, file=f)  # печать элементов в файл
    if timer:
        print("Words count result in created file - out.txt")
    end = time.time()  # окончание таймера
    if timer:  # вывод времени выполнения в случае если таймер = True
        print("Words count execution time = " + str((end - start))[0:5] + " seconds")  # вывод результата таймера
    return alice_dict  # функция возвращает словарь для работы с ним в другой фукнции


def words_rating():  # функция для часто встречающихся слов
    start = time.time()  # начало таймера

    n = input("Input N: ")  # ввод числа самых встречающихся переменных
    n = int(n)  # обработка вводного символа как числа

    alice_dict = words_count(timer=False)  # получение словаря
    alice_dict_sorted = (sorted(alice_dict.items(), key=lambda x: x[1]))  # получение отсортированного списка
    alice_length = (len(alice_dict_sorted))  # длинна списка

    alice_words_rating = alice_dict_sorted[(int(alice_length)-n):int(alice_length)]  # срез списка от последнего минус
    # указанное число до самого последнего
    for item in reversed(alice_words_rating):  # вывод реверсивного списка
        print(item)

    end = time.time()  # окончание таймера
    print("Words rating execution time = " + str((end - start))[0:5] + " seconds")  # вывод результата таймера


words_count()  # запуск функции подсчета слов
words_rating()  # запуск функции часто встречающихся слов
