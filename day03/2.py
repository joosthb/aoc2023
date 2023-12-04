import re

def ispartnumber(environment: list) -> bool:
    for inchar in environment:
        if inchar != '.' and not inchar.isdigit():
            return True
    return False

with open('testinput', 'r', encoding="utf-8") as fp:
    lines = fp.read().splitlines()

repatern = re.compile(r'\*')

total = 0

for y, line in enumerate(lines):
    matches = repatern.finditer(line)
    for match in matches:
        for yy in range(y-1, y+2):
            for xx in range(match.span()[0]-1, match.span()[0]+2):
                print(lines[yy][xx])
        # print(y, match.span()[0])
        # print(lines[y][match.span()[0]])

    
        # start = max(match.start()-1, 0)
        # end = min(match.end()+1, len(line))

        # adjacent = []
        # if y:
        #     adjacent += lines[y-1][start:end]
        # adjacent += line[start:end]
        # if y + 1 < len(lines):
        #     adjacent += lines[y+1][start:end]
        # if ispartnumber(adjacent):
        #     total += int(match.group())

print(total)