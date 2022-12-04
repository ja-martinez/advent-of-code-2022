def calculate_priority(item):
    if ord(item) > 90:      # if it's lowercase from ASCII
        return ord(item) - 96
    
    return ord(item) - 64 + 26      # +26 to account for extra uppercase priority

def solve_part1():
    with open('3/input.txt') as f:
        rucksacks = list(map(lambda el: el.strip(), f.readlines()))
        sum = 0
        
        for rucksack in rucksacks:
            compartment_1 = rucksack[0:len(rucksack)//2]
            compartment_2 = rucksack[len(rucksack)//2:]
            compartment_1_set = set(compartment_1)
            
            for item_in_2 in compartment_2:
                if (item_in_2 in compartment_1_set):
                    sum += calculate_priority(item_in_2)
                    break
    
    return sum


def solve_part2():
    with open('3/input.txt') as f:
        rucksacks = list(map(lambda el: el.strip(), f.readlines()))
        sum = 0
        
        # iterate over groups
        for group_index in range(0, len(rucksacks), 3):
            group_rucksacks = rucksacks[group_index:group_index+3]
            
            # put each rucksack's data in set
            group_rucksacks_sets = []
            for rucksack in group_rucksacks:
                items_set = set(list(rucksack))
                group_rucksacks_sets.append(items_set)
            
            # get element that appears in each rucksack    
            (badge,) = group_rucksacks_sets[0].intersection(*group_rucksacks_sets)
            
            sum += calculate_priority(badge)

    return sum

print(solve_part1())
print(solve_part2())