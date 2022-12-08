f = open("input.txt", "r")
inputs = f.read()

## Part 1
def full_overlap(assignment1, assignment2):
    if (set(assignment1).issubset(set(assignment2))) or (set(assignment2).issubset(set(assignment1))):
        return True
    else:
        return False

def parse_input(inputs):
    assignments = []
    for assignments_binome in inputs.split('\n'):
        assignment = []
        for assignment_individual in assignments_binome.split(','):
            start,end = list(map(int,assignment_individual.split('-')))
            assignment.append(list(range(start,end+1)))    
        assignments.append(assignment)
    return assignments

assignments = parse_input(inputs)
fully_contained = [full_overlap(assignment1, assignment2) for assignment1, assignment2 in assignments]

print('Sum of pairs with full overlap : ',sum(fully_contained))

## Part 2
def partial_overlap(assignment1, assignment2):
    if (len(set(assignment1) & set(assignment2)) > 0 ):
        return True
    else:
        return False

partialy_contained = [partial_overlap(assignment1, assignment2) for assignment1, assignment2 in assignments]

print('Sum of pairs with partial overlap : ',sum(partialy_contained))

