import math

def parse_input():
    with open('8/input.txt') as f:
        lines = f.readlines()
        
    grid = [list(line.strip()) for line in lines]
    
    return grid

def check_visible(location: tuple[int], grid: list[list], memo: dict[tuple, bool]):
    if tuple in memo:
        return memo[tuple]
    
    x, y = location
    
    # if its on edge of grid
    if (x == 0 or y == 0 or x == len(grid) or y == len(grid[0])):
        memo[location] = False
        return False
    
    
    

def solve_part1():
    grid = parse_input()
    not_visible_count = 0
    # visible_count = len(grid) * 2 + len(grid[0]) * 2 - 4

    for i in range(1, len(grid) - 1):   # rows
        row = grid[i]
        
        for j in range(1, len(grid[0]) - 1):    # cols
            column = [curr_row[j] for curr_row in grid]
            curr_height = grid[i][j]
            
            # check up
            col_above = column[0:i]
            if (curr_height > max(col_above)):
                continue
            
            # check down
            col_below = column[i+1:]
            if (curr_height > max(col_below)):
                continue
            
            # check left
            row_left = row[0:j]
            if (curr_height > max(row_left)):
                continue
            
            # check right
            row_right = row[j+1:]

            if (curr_height > max(row_right)):
                continue

            not_visible_count += 1
            
    visible_count = len(grid) * len(grid[0]) - not_visible_count

    return visible_count

def get_viewing_distance(curr_height, trees):
    for i in range(len(trees)):
        if (trees[i] >= curr_height):
            break
    
    viewing_distance = i + 1    # trees that loop iterated
    return viewing_distance

def solve_part2():
    grid = parse_input()
    # visible_count = len(grid) * 2 + len(grid[0]) * 2 - 4
    max_score = 0

    # skipping outer trees since they have score 0
    for i in range(1, len(grid) - 1):   # rows
        row = grid[i]
        
        for j in range(1, len(grid[0]) - 1):    # cols
            column = [curr_row[j] for curr_row in grid]
            curr_height = grid[i][j]
            distances = [0] * 4
            
            # check up
            col_above = column[i-1::-1]     # reversed to go bottom->up
            distances[0] = get_viewing_distance(curr_height, col_above)
            
            # check down
            col_below = column[i+1:]
            distances[1] = get_viewing_distance(curr_height, col_below)
            
            # check left
            row_left = row[j-1::-1]     # reversed to go right->left
            distances[2] = get_viewing_distance(curr_height, row_left)
            
            # check right
            row_right = row[j+1:]
            distances[3] = get_viewing_distance(curr_height, row_right)

            score = math.prod(distances)
            if (score > max_score):
                max_score = score

    return max_score

print(solve_part1())
print(solve_part2())