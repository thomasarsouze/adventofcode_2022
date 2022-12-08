f = open("input.txt", "r")
inputs = f.read()

## Part 1
def move(instructions):
    nb_moves, origin, arrival = instructions
    cranes = stacks[origin-1][-nb_moves:]
    del stacks[origin-1][len(stacks[origin-1]) - nb_moves:]
    stacks[arrival-1] += cranes[::-1]

def parse_input(inputs):
    initial_stacks, instructions = inputs.split('\n\n')
    nb_stacks = len(initial_stacks.split('\n')[-1].split('   '))
    positions = []
    for l in initial_stacks.split('\n')[-2::-1]:
        for i in range(0,len(l),4):
            positions.append(l[i+1])
    stacks = [ [] for _ in range(nb_stacks)]
    for i, c in enumerate(positions):
        if c != ' ':
            stacks[i % nb_stacks].append(c)
    instructions = [[int(instruction.split(' ')[i]) for i in [1,3,5]] 
              for instruction in instructions.split('\n')]
    return stacks, instructions

stacks, instructions = parse_input(inputs)
for instruction in instructions:
    move(instruction)
top_stack = ''
for stack in range(len(stacks)):
    top_stack+=stacks[stack][-1]

print('Top of the stacks cranes : ', top_stack)

## Part 2
def partial_overlap(assignment1, assignment2):
    if (len(set(assignment1) & set(assignment2)) > 0 ):
        return True
    else:
        return False

partialy_contained = [partial_overlap(assignment1, assignment2) for assignment1, assignment2 in assignments]

print('Sum of pairs with partial overlap : ',sum(partialy_contained))

