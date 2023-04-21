array = [3,5,-4,8,11,1,-1,6]
targetSum = 10


##def twoNumberSum(array, targetSum):
##    # Write your code here.
##    output = list()
##    for i in range(len(array) - 1):
##        for j in range(i+1, len(array)):
##            if array[i] + array[j] == targetSum:
##                output.append(array[i])
##                output.append(array[j])
##                return output
##

            

def twoNumberSum(array, targetSum):
    # Write your code here.
    output = list()
    for i in array:
        for j+1 in array:
            k = i + j
            if k == targetSum:
                return [i,j]
    return []
			
