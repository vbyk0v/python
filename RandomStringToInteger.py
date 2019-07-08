import re

str = 'temp:# 42abc'

def rs(string_to_parse, one_number=True):
    if one_number:
        result = re.findall(r'\d+', string_to_parse)
        numb = int(result[0])
        print(type(numb))
        return numb
    elif not one_number:
        pass


print(rs(string_to_parse=str))
