def is_isogram(string):

    letters = dict()
    for i in string.casefold():
        letters[i] = letters.get(i,0)+1

    for i in letters:
        if letters.get(i) > 1:
            return print("not isogram")

    return print("is isogram")

help
