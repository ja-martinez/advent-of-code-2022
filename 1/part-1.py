# Solution to first part of problem

maxCalories = 0
with open('1/input.txt') as f:
    currCalories = 0
    while True:
        line = f.readline()
        
        if line.strip():    # if line contains a number
            currCalories += int(line.strip())
            continue
            
        if currCalories > maxCalories:
            maxCalories = currCalories
                
        currCalories = 0
        
        if not line:    # if line is empty string -> EOF
            break
        
    print(maxCalories)
