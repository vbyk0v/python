# set = {1,2,3,4,5,6}
# print(set)
#
# # set.update([1,7],{1,8})
# # print(set)
#
# set.discard(4)
# print(set)
#
# set.remove(9)
# print(set)


a = {0,1,3,5,7,9}
b = {0,2,4,6,8,10}

def set_operations():
    """
    объединение
    """
    print(a | b)
    print(a.union(b))
    print(b.union(a))

    """
    пересечение
    """
    print(a&b)
    print(a.intersection(b))

    """
    разница
    """
    print(b-a)
    print(a.difference(b))

    """
    симметричная разница
    """
    print(a.symmetric_difference(b))

def set_operations_2():
    a = {'apple'}
    b = set('brownie')

    print('a' in a)
    print('p' not in a)
    for letter in a:
        print(letter)

    print('b' in b)
    print('z' not in b)
    for letter in b:
        print(letter)

set_operations_2()