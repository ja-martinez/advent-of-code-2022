def check_enclosing(range1, range2):
    """ Checks if range1 encloses range2
    """
    
    # check lower bound
    if range1[0] > range2[0]:
        return False
    
    # check lower bound
    if range1[1] < range2[1]:
        return False
    
    return True

def solve_part1():
    count = 0
    
    # iterate over pairs
    for line in open('4/input.txt'):
        # put pairs in list of ranges
        pair = list(map(lambda range_str: range_str.strip().split('-'), line.split(',')))
        # cast ranges as ints
        pair = [[int(bound) for bound in range] for range in pair]
        
        if (check_enclosing(pair[0], pair[1]) or check_enclosing(pair[1], pair[0])):
            count += 1
        
    return count

def check_overlap(pair):
    range1, range2 = pair
    # if overlap, then one's upper-bound is greater than other's lower-bound
    if (range1[1] < range2[0] or range2[1] < range1[0]):
        return False
    
    return True

def solve_part2():
    count = 0
    
    # iterate over pairs
    for line in open('4/input.txt'):
        # put pairs in list of ranges
        pair = list(map(lambda range_str: range_str.strip().split('-'), line.split(',')))
        # cast ranges as ints
        pair = [[int(bound) for bound in range] for range in pair]
        
        if check_overlap(pair):
            count += 1
        
    return count

print(solve_part1())
print(solve_part2())