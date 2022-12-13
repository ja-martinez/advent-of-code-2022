

def solve_part1():
    with open('6/input.txt') as f:
        input = f.readlines()[0]
        
    last3 = []
        
    for i in range(len(input)):
        value = input[i]
        
        try:    # val is not unique
            value_index = last3.index(value)
            last3 = last3[value_index + 1:] + [value]
        except:     # val is unique
            if len(last3) == 3:
                return i + 1
            
            last3.append(value)
            
def solve_part2():
    with open('6/input.txt') as f:
        input = f.readlines()[0]
        
    last3 = []
        
    for i in range(len(input)):
        value = input[i]
        
        try:    # val is not unique
            value_index = last3.index(value)
            last3 = last3[value_index + 1:] + [value]
        except:     # val is unique
            if len(last3) == 13:
                return i + 1
            
            last3.append(value)
        
        
print(solve_part1())
print(solve_part2())