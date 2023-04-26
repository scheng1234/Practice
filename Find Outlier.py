def find_outlier(integers):
    evens = list(filter(lambda x: (x%2 == 1), integers))
    odds = list(filter(lambda x: (x%2 == 0), integers))
    
    if len(evens) == 1:
        sol = evens[0]
    else:
        sol = odds[0]

    return sol

def find_outlier2(integers):
    assert len(integers) >= 3

    bit = integers[0] & 1
    print(integers, bit)
    if integers[1] & 1 != bit:
        return integers[integers[2] & 1 == bit]

    for n in integers:
        print(n)
        if n & 1 != bit:
            print(n&1)
            return n

    assert False