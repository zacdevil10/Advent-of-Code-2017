list = list(map(int, open('input/day5.txt').readlines()))

jumps = steps = 0

while jumps < len(list):
    h = list[jumps]
    list[jumps] -= 1 if list[jumps] >= 3 else -1
    jumps += h
    steps += 1

print("Part 2:", steps)
