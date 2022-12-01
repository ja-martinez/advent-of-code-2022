# Similar to part-1, but now we have to keep track of 3 largest calorie counts
from functools import reduce

def try_insert(sorted_list, new_num):
    """tries to number into a sorted list of maximum numbers
    """
    for i in range(len(sorted_list)):
        if new_num >= sorted_list[i]:
            sorted_list.pop()   # we have to drop smallest value to maintain length
            sorted_list.insert(i, new_num)
            return

largest = [0,0,0]
    
with open('1/input.txt') as f:
    currCal = 0
    
    while True:
        line = f.readline()
        
        if line.strip():    # if line contains a number
            currCal += int(line.strip())
            continue
        
        try_insert(largest, currCal)
        currCal = 0
        
        if not line:
            break
    
sum = reduce(lambda a,b: a+b, largest)
print(sum)