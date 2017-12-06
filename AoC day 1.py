total1 = 0
total2 = 0
sequence = str(1122) #Put any sequence here
length = len(sequence)

for x in range(length):
    n = int((x + 1) % length)
    total1 += int(sequence[x]) if sequence[x] == sequence[n] else 0
print("Part 1:", total1)

for x in range(length):
    n = int((x + (length/2)) % length)
    total2 += int(sequence[x]) if sequence[x] == sequence[n] else 0
print("Part 2:", total2)
