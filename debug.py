#debug tests that I needed to do
#This will most likely be removed in the initial release.

#$help hall

def separate_str(cmdstr):
    counter = 1
    building_word = ''
    word_list = []
    for char in cmdstr:
        if counter != 1:
            if char == " ":
                if building_word != '':
                    word_list.append(building_word)
                building_word = ''
            elif char == "$":
                pass
            else:
                building_word += char
                    
        else:
            if char != "$":
                return False
        counter += 1
    if building_word != '':
        word_list.append(building_word)
    return word_list

print(separate_str('$help hall'))

