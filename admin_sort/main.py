# -*- coding: utf8 -*-

def sort_me():
    result = ''
    with open('to_sort.txt', encoding='utf-8-sig') as txt:
        for line in txt:
            result = result + str(line)
    result_list = result.split(';')
    result_list_2 = []
    for d in range(0, len(result_list)):
        result_list_2.append(result_list[d].split('\\'))
    with open('sorted.txt', 'w') as file:
        for d in range(0, len(result_list_2)-1):
            file.write("%s\n" % result_list_2[d][1])


if __name__ == "__main__":
    sort_me()
