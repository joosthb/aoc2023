import re
with open('input', 'r', encoding="utf-8") as fp:
    lines = fp.read().splitlines()

cardcounter = [1 for x in lines]

for line in lines:
    cardidstr, card = line.split(': ')
    cardindex = int(re.findall(r'\d+', cardidstr)[0])-1
    # calculate matching numbers
    winning, having = card.split(' | ')
    swinning = set(winning.split(' ')).difference(set(['']))
    shaving = set(having.split(' ')).difference(set(['']))
    matches = len(shaving.intersection(swinning))
    # add cards to stack
    for i in range(cardcounter[cardindex]):
        for y in range(cardindex + 1, cardindex + matches + 1):
            cardcounter[y] += 1

print(sum(cardcounter))
