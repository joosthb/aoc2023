with open('input', 'r', encoding="utf-8") as fp:
    lines = fp.read().splitlines()

total = 0

for line in lines:
    winning, having = line.split(': ')[1].split(' | ')
    swinning = set(winning.split(' ')).difference(set(['']))
    shaving = set(having.split(' ')).difference(set(['']))
    matches = len(shaving.intersection(swinning))
    if matches > 0:
        total += 2**(matches-1)
print(total)
