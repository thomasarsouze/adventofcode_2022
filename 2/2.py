f = open("input.txt", "r")
inputs = f.read()

win = {'rock': 'scissor', 'paper': 'rock', 'scissor': 'paper'}
translate = {'A': 'rock', 'B': 'paper', 'C': 'scissor', 'X': 'rock', 'Y': 'paper', 'Z': 'scissor'}

points_shape = {'rock': 1, 'paper': 2, 'scissor': 3}
points_outcome = {'lost': 0, 'draw': 3, 'won': 6}

## Part 1

def outcome(opponent_play, my_play):
    if translate[opponent_play] == translate[my_play]:
        return 'draw'
    elif win[translate[opponent_play]] == translate[my_play]:
        return 'lost'
    else:
        return 'won'

def calculate_points(opponent_play, my_play):
    return points_shape[translate[my_play]] + points_outcome[outcome(opponent_play, my_play)]

points = [ calculate_points(round.split()[0],round.split()[1])
    for round in inputs.split('\n')
]

total_points = sum(points)
print('Total points won : ', total_points)


## Part 2

dict_outcome = {'X': 'lost', 'Y': 'draw', 'Z': 'won'}

def determine_my_play(opponent_play, outcome):
    if dict_outcome[outcome] == 'draw':
        return translate[opponent_play]
    elif dict_outcome[outcome] == 'lost':
        return win[translate[opponent_play]]
    else:
        key = [k for k, v in win.items() if v == translate[opponent_play]][0]
        return key

points = []
for round in inputs.split('\n'):
    my_play = determine_my_play(round.split()[0],round.split()[1])
    points.append(points_shape[my_play] + points_outcome[dict_outcome[round.split()[1]]])

total_points = sum(points)
print('Total points won : ', total_points)
