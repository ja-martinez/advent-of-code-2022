"""
PARSING DATA:
* Stack starting point and instructions are separated by an empty line
* stacks separated  with themselves by one space
* have to determine number of stacks
* the letters are placed at indeces 1, 5, 9, ... so separated by 4
"""

import re

def get_initial_stacks(stack_data, stack_names):
    
    stacks = [[] for name in stack_names if name != " "]
    
    # fill stacks with data
    for level in reversed(stack_data):
        # iterate over each column data
        i = 0
        curr_stack = 0
        curr_crate = ""

        while (i < len(level)):
            char = level[i]

            # if level is empty for stack, skip to next stack
            if char == " ":
                i += 4
                curr_stack += 1
                continue

            if char == '[':
                i += 1
                continue

            if char == ']':
                stacks[curr_stack].append(curr_crate)
                curr_stack += 1
                curr_crate = ""
                i += 2
                continue

            curr_crate += char
            i += 1
            
    return stacks

def solve_part1():
    with open('5/input.txt') as f:
        lines = list(map(lambda el: el.strip('\n'), f.readlines()))

    # separate instructions and stacks by empty line
    separation_index = lines.index('')
    stack_data = lines[:separation_index - 1]
    stack_names = lines[separation_index - 1]
    instructions = lines[separation_index + 1:]
    
    # fill stacks with data
    stacks = get_initial_stacks(stack_data, stack_names)

    for instruction in instructions:
        instruction_nums = re.findall('\d+', instruction)
        count, origin_name, destination_name = [int(num) for num in instruction_nums]
        origin = stacks[origin_name - 1]
        destination = stacks[destination_name -1]

        # move the elements
        for _ in range(count):
            destination.append(origin.pop())
            
    solution = ""
    
    for stack in stacks:
        solution += stack[-1]
        
    return solution

def solve_part2():
    with open('5/input.txt') as f:
        lines = list(map(lambda el: el.strip('\n'), f.readlines()))

    # separate instructions and stacks by empty line
    separation_index = lines.index('')
    stack_data = lines[:separation_index - 1]
    stack_names = lines[separation_index - 1]
    instructions = lines[separation_index + 1:]

    stacks = get_initial_stacks(stack_data, stack_names)

    for instruction in instructions:
        instruction_nums = re.findall('\d+', instruction)
        count, origin_name, destination_name = [int(num) for num in instruction_nums]
        origin = stacks[origin_name - 1]
        destination = stacks[destination_name -1]

        # move the elements
        destination.extend(origin[-count:])
        del origin[-count:]

    solution = ""
    for stack in stacks:
        solution += stack[-1]
        
    return solution

print(solve_part1())
print(solve_part2())