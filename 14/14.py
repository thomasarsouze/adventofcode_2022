
def solve(rocks, sand_origin):    
    deepest_rock = max(m[1] for m in rocks)
    sand_moves = [(0, 1), (-1, 1), (1, 1)]
    sand = []
    sand_position = sand_origin

    while sand_position[1] < deepest_rock:
        for move in sand_moves:
            next_sand_position = (sand_position[0] + move[0],sand_position[1] + move[1])
            if next_sand_position not in rocks and next_sand_position not in sand:
                sand_position = next_sand_position
                break
        else:
            sand.append(sand_position)
            sand_position = sand_origin
    return len(sand)

def parse_input(inputs):
    rocks = []
    for r in inputs.split("\n"):
        coords = [tuple(map(int, j.split(","))) for j in r.split(" -> ")]
        for i in range(len(coords) - 1):
            x1, y1 = coords[i]
            x2, y2 = coords[i+1]
            if x1 == x2:
                # vertical line
                y_values = list(range(min(y1, y2), max(y1, y2)+1))
                for y in y_values:
                    rocks.append((x1, y))
            elif y1 == y2:
                # horizontal line
                x_values = list(range(min(x1, x2), max(x1, x2)+1))
                for x in x_values:
                    rocks.append((x, y1))
    return rocks


f = open("14/input.txt", "r")
inputs = f.read()
rocks = set(parse_input(inputs))
sand_origin = (500,0)

print(solve(rocks, sand_origin))

# Very slow !
def solve2(rocks, sand_origin):    
    deepest_rock = max(m[1] for m in rocks)
    sand_moves = [(0, 1), (-1, 1), (1, 1)]
    sand = []
    sand_position = sand_origin
    ground = deepest_rock + 2

    while sand_origin not in sand:
        for move in sand_moves:
            next_sand_position = (sand_position[0] + move[0],sand_position[1] + move[1])
            if next_sand_position not in rocks and next_sand_position not in sand and next_sand_position[1] < ground:
                sand_position = next_sand_position
                break
        else:
            sand.append(sand_position)
            print(len(sand))
            sand_position = sand_origin
    return len(sand)

print(solve2(rocks, sand_origin))

