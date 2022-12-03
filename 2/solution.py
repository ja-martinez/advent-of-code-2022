"""
    PART 1 Meaning of letters 
    (A, B, C) -> (Rock, Paper, Scissors) -> (X, Y, Z)
    
    PART 2 Meaning of letters
    (A, B, C) -> (Rock, Paper, Scissors)
    (X, Y, Z) -> you need to (lose, draw, win)
    
    Points
    (X, Y, Z) -> (1, 2, 3)
    (Loss, Draw, Win) -> (0, 3, 6)
"""

shape_points = {
    'A': 1,
    'B': 2,
    'C': 3
}

equivalent_shapes = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

# maps key to shape needed to win
win_shapes = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

lose_shapes = {v: k for k, v in win_shapes.items()}

def calculate_score(round_shapes):
    """Calculates score given standardized shapes
    """
    opponent_shape, your_shape = round_shapes
    score = shape_points[your_shape]
    
    # Check if there's a tie or win
    if your_shape == opponent_shape:
        score += 3
    elif win_shapes[your_shape] == opponent_shape:
        score += 6
    
    return score

def solve_part1():
    total_score = 0
    
    for line in open('2/input.txt'):
        shapes = line.split();
        shapes[1] = equivalent_shapes[shapes[1]] # standardize your shape
        total_score += calculate_score(shapes)
        
    return total_score

def solve_part2():
    total_score = 0
    
    for line in open('2/input.txt'):
        data = line.split();

        opponent_shape, result = data
        if (result == 'X'):     # you lose
            shapes = [opponent_shape, win_shapes[opponent_shape]]
        elif (result == 'Y'):   # you tie
            shapes = [opponent_shape, opponent_shape]
        elif (result == 'Z'):   # you win
            shapes = [opponent_shape, lose_shapes[opponent_shape]]
            
        total_score += calculate_score(shapes)
        
    return total_score

print(solve_part1())
print(solve_part2())