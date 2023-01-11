from math import lcm

f = open("input.txt", "r")
inputs = f.read()

class Monkey:
    def __init__(self, id) -> None:
        self.worry_level = 0
        self.id = id
        self.items = []
        self.nb_inspects = 0
        
    def _add_item(self, value):
        self.items.append(value)

    def _define_operation(self, operator, value):
        if value == 'old':
            if operator =='+':
                self.operation = lambda x: x + x
            else:
                self.operation = lambda x: x * x
        else:
            if operator =='+':
                self.operation = lambda x: x + int(value)
            else:
                self.operation = lambda x: x * int(value)
                
    def _define_test_and_target(self, test_value, target_true, target_false):
        self.test_value = test_value
        self.target_true = target_true
        self.target_false = target_false
        
    def test_and_target(self):
        if (self.worry_level % self.test_value == 0):
            return self.target_true
        else:
            return self.target_false

def parse_input(inputs):
    monkeys = []
    for m in inputs.split('\n\n'):
        monkey_description = m.split('\n')
        monkey=Monkey(int(monkey_description[0][-2]))
        # Get list of items
        for i in [*map(int, monkey_description[1].split(":")[1].strip().split(", "))]:
            monkey._add_item(i)
        # Get operation for worry_level
        _, operator, value = monkey_description[2].split("=")[1].strip().split()
        monkey._define_operation(operator, value)
        # Do the test and choose target
        monkey._define_test_and_target(int(monkey_description[3].split()[-1]),
                                      int(monkey_description[4].split()[-1]),
                                      int(monkey_description[5].split()[-1]))
        
        monkeys.append(monkey)
    return monkeys
    
monkeys = parse_input(inputs)

## Part 1
nb_rounds = 20
for _ in range(nb_rounds):
    for m in monkeys:
        while m.items:
            m.nb_inspects += 1
            m.worry_level = m.items.pop(0)
            m.worry_level = m.operation(m.worry_level)
            m.worry_level //= 3
            monkeys[m.test_and_target()]._add_item(m.worry_level)

monkeys_inspections = sorted([m.nb_inspects for m in monkeys])

print("Monkey business level : ", monkeys_inspections[-1] * monkeys_inspections[-2])

## Part 2

monkeys = parse_input(inputs)

nb_rounds = 10000
reduce_worry_value = lcm(*[m.test_value for m in monkeys])
for i in range(nb_rounds):
    if (i % 500 == 0): print(i)
    for m in monkeys:
        while m.items:
            m.nb_inspects += 1
            m.worry_level = m.items.pop(0)
            m.worry_level = m.operation(m.worry_level)
            m.worry_level %= reduce_worry_value
            monkeys[m.test_and_target()]._add_item(m.worry_level)

monkeys_inspections = sorted([m.nb_inspects for m in monkeys])

print("Monkey business level : ", monkeys_inspections[-1] * monkeys_inspections[-2])    
