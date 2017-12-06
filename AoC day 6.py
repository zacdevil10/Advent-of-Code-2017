with open('input/day6.txt') as f:
    list = [int(x) for x in f.read().strip().split()]

prev = []

while list not in prev:
    prev.append(list[:])
    highest = max(list)
    i = list.index(highest)
    list[i] = 0
    for x in range(highest):
          i += 1
          list[i % len(list)] += 1

print("Part 1:", len(prev), "Part 2:", len(prev) - prev.index(list))
