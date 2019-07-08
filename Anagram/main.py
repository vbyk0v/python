# -*- coding: utf8 -*-


def main():
    text = prepare_text()
    anagram = input("Enter the word: ")
    check_anagram(text, anagram)


def prepare_text():
    a_string = ''  # создание пустой строки
    with open('alice.txt', encoding='utf-8-sig') as txt:  # открыть текстовый файл в кодировке utf-8
        for line in txt:  # перебор строк в открытом файле
            a_string = a_string + str(line)  # в пустую строку приплюсовывать все строки из файла

    string_filter = str.maketrans(dict.fromkeys(".,!;:'’‘)(?"))  # создание фильтра специальных символов
    b_string = a_string.translate(string_filter)  # применение фильтра к строке
    c_string = b_string.lower()  # преобразование всех прописных букв в строчные
    d_string = c_string.replace("-", " ")  # замена тире на пробел
    words = d_string.split()  # создание из строки списка где каждое слово является элементом списка
    return words


def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()
    return (list_str1 == list_str2)


def check_anagram(words, anagram):
    for word in words:
        if is_anagram(word, anagram) == True and word != anagram:
            print(word)


if __name__ == "__main__":
    main()
