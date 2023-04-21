def row_sum_odd_numbers(n):

    i=n
    l = list()
    while i > 1:
        i -= 1
        l.append(i*2)
        
    return sum(l)+ (1+sum(l))*n
