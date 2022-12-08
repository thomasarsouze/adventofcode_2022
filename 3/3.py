import string

f = open("input.txt", "r")
inputs = f.read()

priorities = {l: i+1 for i,l in enumerate(list(string.ascii_lowercase)+list(string.ascii_uppercase))}

## Part 1

double_items = []
for rucksack in inputs.split('\n'):
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    double_items.append(list(set(compartment1) & set(compartment2))[0])

double_items_priorities = [priorities[i] for i in double_items]

print('Sum of the priorities of items in the 2 compartments is : ',sum(double_items_priorities))


## Part 2
def groups(rucksacks, n):
    for i in range(0, len(rucksacks), n):
        yield rucksacks[i:i + n]

rucksacks_groups = list(groups(inputs.split('\n'), 3))
common_items = [list(set(r1) & set(r2) & set(r3))[0] for r1, r2, r3 in rucksacks_groups]

common_items_priorities = [priorities[i] for i in common_items]
print('Sum of the priorities of common items in each group : ',sum(common_items_priorities))
