import heapq

f = open("input.txt", "r")
inputs = f.read()
calories = [
    [int(ration) for ration in elf.split('\n')]
    for elf in inputs.split('\n\n')
]
calories_per_elf = [sum(per_elf) for per_elf in calories]
top_calories = max(calories_per_elf)
print('Most calories carried by an elf is : ', top_calories)

top3_calories = sum(heapq.nlargest(3, calories_per_elf))
print('Top 3 most calories carried by elves is : ', top3_calories)
