BOOL = list()
SEQ = list()
sequence = [6, -1, 1, 23]
array = [5, 1, 22, 25, 6, -1, 8, 10]

for i in range(0,len(sequence)):
        BOOL.append(sequence[i] in array)
        print(BOOL)
        print(all(BOOL))
        if all(BOOL):
            SEQ.append(array.index(sequence[i]))
            print(SEQ)
                       
