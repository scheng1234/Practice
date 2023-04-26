def solution(text, ending):
    sol = list()

    if(len(ending) > len(text)):
        return(False)
    
    for a in range(len(ending)):
        
        if text[-a-1] == ending[-a-1]:
            sol.append(True)
            continue
        else:
            sol.append(False)

    return(all(sol))
