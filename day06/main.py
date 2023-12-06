from math import prod

# time, distance pairs
chalinput = {'testinput': [[7, 9], [15, 40], [30, 200]], 'prodinput': [[56, 499], [97, 2210], [77, 1097], [93, 1440]], 'testinput2': [[71530, 940200]], 'prodinput2': [[56977793, 499221010971440]] }

if __name__ == "__main__":
    wins = []
    for type, scores in chalinput.items():
        for time, record in scores:
            ways = 0
            for x in range(1, time):
                # increase ways to win if distance exceeds record
                ways += 1 if x*(time-x) > record else 0
            wins += [ways]
        print(type, prod(wins))
