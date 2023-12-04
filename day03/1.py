import re

def ispartnumber(environment: list) -> bool:
    for inchar in environment:
        if inchar != '.' and not inchar.isdigit():
            return True
    return False

with open('input', 'r', encoding="utf-8") as fp:
    lines = fp.read().splitlines()

repatern = re.compile(r'\d+')

total = 0

for y, line in enumerate(lines):
    matches = repatern.finditer(line)
    for match in matches:
        start = max(match.start()-1, 0)
        end = min(match.end()+1, len(line))

        adjacent = []
        if y:
            adjacent += lines[y-1][start:end]
        adjacent += line[start:end]
        if y + 1 < len(lines):
            adjacent += lines[y+1][start:end]
        if ispartnumber(adjacent):
            total += int(match.group())

print(total)