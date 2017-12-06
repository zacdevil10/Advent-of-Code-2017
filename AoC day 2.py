import itertools

with open('input/day2.txt', 'r') as f:
    lines = [x.strip().split() for x in f.read().splitlines()]

checksum1, checksum2 = 0, 0

for row in lines:
    num = list(map(int, row))
    checksum1 += max(num) - min(num)

    for i in itertools.combinations(num, 2):
        checksum2 += max(i) / min(i) if max(i) % min(i) == 0 else 0

print(checksum1, checksum2)
