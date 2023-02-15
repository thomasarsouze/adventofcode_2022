def dist(A,B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def solve(row, sensor_data):
    impossible_positions = set()
    for S, B in sensor_data:
        closest_beacon_dist = dist(S,B)
        for x in range(S[0]-closest_beacon_dist, S[0]+closest_beacon_dist+1):
            dist_point = dist(S,(x, row))
            if dist_point <= closest_beacon_dist:
                impossible_positions.add(x)
    return impossible_positions

def parse_input(inputs):
    sensors_and_beacons = []
    for line in inputs.split("\n"):
        sensors_and_beacons.append([tuple(tuple(map(lambda x: int(x[2:]), l.split()[-2:])))
                                    for l in line.replace(",", "").split(':')])
    return sensors_and_beacons


f = open("15/input.txt", "r")
inputs = f.read()
sensor_data = parse_input(inputs)
# Part 1
impossible_positions = solve(10,sensor_data)
print(len(impossible_positions)-1)

# Part 2
def solve2(sensor_data, limit):
    for y in range(limit+1):
        ranges = []
        for S, B in sensor_data:
            closest_beacon_dist = dist(S,B)
            dist_x = closest_beacon_dist - abs(y-S[1])
            if dist_x >= 0:
                ranges.append((max(0,S[0]-dist_x), min(limit,S[0]+dist_x)))
                
        ranges.sort()

        min_range, max_range = ranges[0]
        if min_range > 0: return y
        for i in range(1, len(ranges)):
            if ranges[i][0] <= max_range:
                max_range = max(max_range, ranges[i][1])
            else:
                return (max_range+1) * 4000000 + y
    
print(solve2(sensor_data, 4000000))
