def compare_ints(a,b):
    if a == b: return 'equal'
    if a < b: return 'smaller'
    if a > b: return 'greater'

def compare_lists(left, right):
    i = 0
    compare = 'equal'
    while (i < min(len(left), len(right))) and (compare == 'equal'):
        if isinstance(left[i], int) and isinstance(right[i], int):
            compare = compare_ints(left[i], right[i])
        elif isinstance(left[i], list) and isinstance(right[i], list):
            compare = compare_lists(left[i], right[i])
        elif isinstance(left[i], list) and isinstance(right[i], int):
            compare = compare_lists(left[i], [right[i]])
        elif isinstance(left[i], int) and isinstance(right[i], list):
            compare = compare_lists([left[i]], right[i])
        i += 1
    if (compare == 'equal') and (len(right) != len(left)):
        if i == len(left): compare = 'smaller'
        if i == len(right): compare = 'greater'
    return compare

def solve(pairs):
    right_order = []
    for i, (left, right) in enumerate(pairs):
        if compare_lists(left, right) == 'smaller':
            print('index '+str(i)+' is in the right order')
            right_order.append(i+1)
    return right_order

def parse_input(inputs: str):
    lines = inputs.strip().split("\n")
    tuples = []
    for first,second in zip(lines[::3],lines[1::3]):
        tuples.append((eval(first), eval(second)))
    return tuples

f = open("input.txt", "r")
inputs = f.read()

# Part 1
pairs = parse_input(inputs)
print(sum(solve(pairs)))

# Part 2
def parse_input2(inputs: str):
    lines = inputs.strip().split("\n")
    tuples = []
    for l in lines:
        if l: tuples.append((eval(l)))
    tuples.append([[2]])
    tuples.append([[6]])
    return tuples

def solve2(packets, divider1, divider2):
    lst = len(packets)
    # Bubble sort
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (compare_lists(packets[j], packets[j + 1]) == 'greater'):
                temp = packets[j]
                packets[j]= packets[j + 1]
                packets[j + 1]= temp
    return (packets.index(divider1)+1)*(packets.index(divider2)+1)

packets = parse_input2(inputs)
solve2(packets,[[2]],[[6]])