from collections import deque


def parse_input(inputs: str):
    lines = inputs.strip().split("\n")
    heightmap = [list(line) for line in lines]
    start, goal = None, None
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 'S':
                start = (i, j)
            if heightmap[i][j] == 'E':
                goal = (i, j)
    return heightmap, start, goal
    
f = open("input.txt", "r")
inputs = f.read() 
heightmap, start, goal = parse_input(inputs)



def solve(heightmap, start, goal):
    heightmap[start[0]][start[1]] = 'a' 
    heightmap[goal[0]][goal[1]] = 'z' 
    rows, cols = len(heightmap), len(heightmap[0])
    distances = [[-1 for j in range(cols)] for i in range(rows)]
    distances[start[0]][start[1]] = 0

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, 0)])
            
    while queue:
        pos, step = queue.popleft()
        if pos == goal:
            return step
        next_pos = [(pos[0] + dy, pos[1] + dx) for dy, dx in dirs]
        for np in next_pos:
            if not 0 <= np[0] < rows or not 0 <= np[1] < cols:
                continue
            if distances[np[0]][np[1]] != -1 and distances[np[0]][np[1]] <= step + 1:
                continue
            if ord(heightmap[np[0]][np[1]]) - ord(heightmap[pos[0]][pos[1]]) > 1:
                continue

            distances[np[0]][np[1]] = step + 1
            queue.append((np, step + 1))
        
## Part 1
print(solve(heightmap, start, goal)) 

#------------------

def solve2(heightmap, start, goal):
    heightmap[start[0]][start[1]] = 'a' 
    heightmap[goal[0]][goal[1]] = 'z' 
    rows, cols = len(heightmap), len(heightmap[0])
    distances = [[-1 for j in range(cols)] for i in range(rows)]
    distances[start[0]][start[1]] = 0

    starts = [(i,j) for j in range(cols) for i in range(rows) if heightmap[i][j]=='a']
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(goal, 0)])
            
    min_steps = 100000
    while queue:
        pos, step = queue.popleft()
        if pos in starts:
            if step < min_steps: min_steps = step
            continue
        if step > min_steps:
            continue
        next_pos = [(pos[0] + dy, pos[1] + dx) for dy, dx in dirs]
        for np in next_pos:
            if not 0 <= np[0] < rows or not 0 <= np[1] < cols:
                continue
            if distances[np[0]][np[1]] != -1 and distances[np[0]][np[1]] <= step + 1:
                continue
            if ord(heightmap[np[0]][np[1]]) - ord(heightmap[pos[0]][pos[1]]) < -1:
                continue

            distances[np[0]][np[1]] = step + 1
            queue.append((np, step + 1))
            
    return min_steps

## Part 2
print(solve2(heightmap, start, goal)) 
