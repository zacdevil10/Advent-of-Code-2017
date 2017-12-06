rows = (open('input/day4.txt').read().strip()).split('\n')

valid1 = valid2 = 0

def maagnar(passwords):
    words = set()
    [words.add(str().join(sorted(word))) for word in passwords]
    
    return len(passwords) == len(words)

for row in rows:
    words = row.split()
    valid1 += 1 if len(words) == len(set(words)) else 0
    valid2 += 1 if maagnar(words) else 0

print("Part 1:", valid1, "Part 2:", valid2)
