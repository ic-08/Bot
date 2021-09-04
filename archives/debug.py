#Used for testing, will most likely be deleted in the release version

def foo(pos=None, *, forcenamed):
    print(pos, forcenamed)

foo(1, forcenamed=2)

def separate_str(string):
    building_word = ''
    word_list = []
    if string != '()' and string != "":
        for char in string:
            if char != " " and char != "(" and char != ")" and char != "," and char != "'" and char != '"':
                building_word += char
            else:
                if building_word != '':
                    word_list.append(building_word)
                    building_word = ''
    return word_list

print(separate_str("('Isaac', 'is', 'ricj')"))
