import re

with open('input', 'r', encoding="utf-8") as fp:
    lines = fp.read().splitlines()

repatern = re.compile(r'\d+')

total = 0
field = {}

for y, line in enumerate(lines):
    matches = repatern.finditer(line)
    for match in matches:
        surroundings = []

        start = max(match.start()-1, 0)
        end = min(match.end()+1, len(line))

        if y:
            surroundings += [(y-1, x) for x in range(start,end)]
        if start:
            surroundings += [(y, start)]
        if end != len(line):
            surroundings += [(y, end-1)]
        if y + 1 < len(lines):
            surroundings += [(y+1, x) for x in range(start, end)]

        for cord in surroundings:
            if lines[cord[0]][cord[1]] == '*':
                if cord in field:
                    field[cord] += [int(match.group())]
                else: 
                    field[cord] = [int(match.group())]

for cord, value in field.items():
    if len(value) == 2:
        total += value[0] * value[1]

print(total)
