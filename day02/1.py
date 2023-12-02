import re
from math import prod

def valid_game(takes: str) -> bool:
    ''' validates game - part 1 '''
    maxcubes = {'red': 12, 'green': 13, 'blue': 14}
    for take in takes.split('; '):
        for colorcount in take.split(', '):
            count, color = colorcount.split(' ')
            if int(count) > maxcubes[color]:
                return False
    return True

def power_game(takes: str) -> int:
    ''' calcs power of game - part 2 '''
    mincubes = {'red': 0, 'green': 0, 'blue': 0}
    for take in takes.split('; '):
        for colorcount in take.split(', '):
            count, color = colorcount.split(' ')
            mincubes[color] = max(mincubes[color], int(count))
    return prod(mincubes.values())

with open('input', 'r', encoding="utf-8") as fp:
    games = fp.read().splitlines()

total, power = 0, 0

for game in games:
    gameid, takes = game.split(': ')
    if valid_game(takes):
        total += int(re.sub(r'[^0-9]', '', gameid))
    power += power_game(takes)
print(f'Part 1: %d\nPart 2: %d' % (total, power))
