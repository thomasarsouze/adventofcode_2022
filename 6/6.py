f = open("input.txt", "r")
inputs = f.read()

## Part 1
def find_marker(data, size):
    for i in range(size, len(data)):
        if len(set(data[i-size:i])) == size:
            return i

marker = find_marker(inputs, 4)

print('Index of the position of the marker is : ', marker)

## Part 2

marker = find_marker(inputs, 14)

print('Index of the position of the marker is : ', marker)