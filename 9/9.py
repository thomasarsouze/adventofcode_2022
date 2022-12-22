f = open("input.txt", "r")
inputs = f.read()

directions = {"R": (1, 0), 
              "L": (-1, 0), 
              "U": (0, 1), 
              "D": (0, -1)
              }

def parse_input(inputs):
    return [[int(i) if i.isdigit() else i for i in l.split()] for l in inputs.split('\n')]

def head_moves(movments):
    positions = [(0,0)]
    for direction, nb_steps in movments:
        for _ in range(nb_steps):
            point = (positions[-1][0] + directions[direction][0], positions[-1][1] + directions[direction][1])
            positions.append(point)
    return positions

def distance(positionA, positionB):
    dx = positionA[0] - positionB[0]
    dy = positionA[1] - positionB[1]
    # Distance is wrong in absolute, but ok here
    return dx, dy, abs(dx)+abs(dy)

def tail_moves(head_positions):
    positions = [(0,0)]
    for head_position in head_positions:
        dx,dy,d = distance(head_position, positions[-1])
        if (d==2) and (abs(dx)==2 or abs(dy)==2):
            point = (positions[-1][0] + dx//2 , positions[-1][1] + dy//2)
            positions.append(point)
        elif (d==3):
            if abs(dx)==2:
                point = (positions[-1][0] + dx//2, positions[-1][1] + dy)
            else:
                point = (positions[-1][0] + dx, positions[-1][1] + dy//2)
            positions.append(point)
        elif (d==4):
            point = (positions[-1][0] + dx//2, positions[-1][1] + dy//2)
            positions.append(point)
        else:
            pass
    return positions

movments = parse_input(inputs)
head_positions = head_moves(movments)
tail_positions = tail_moves(head_positions)

## Part 1
print("Nomber of positions visited by tail : ", len(set(tail_positions)))

## Part 2
for i in range(9):
    tail_positions = tail_moves(head_positions)
    head_positions = tail_positions
print("Nomber of positions visited by tail : ", len(set(tail_positions)))