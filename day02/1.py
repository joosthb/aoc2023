import re

def valid_game(takes: str) -> bool:
    ''' validates game '''
    maxcubes = {'red': 12, 'green': 13, 'blue': 14}
    for take in takes.split('; '):
        for colorcount in take.split(', '):
            count, color = colorcount.split(' ')
            if int(count) > maxcubes[color]:
                return False
    return True

with open('input', 'r', encoding="utf-8") as fp:
    games = fp.read().splitlines()

total = 0

for game in games:
    gameid, takes = game.split(': ')
    if valid_game(takes):
        total += int(re.sub(r'[^0-9]', '', gameid))
print(total)
