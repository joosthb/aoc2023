import re

transtable = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
pattern = r'[^0-9]'
sum = 0

with open('1.txt', 'r') as fp:
    lines = fp.readlines()

for line in lines:
    for number in transtable.items():
        line = line.replace(number[0], number[0] + number[1] + number[0] )
    digits = re.sub(pattern, '', line)
    sum += int(digits[:1])*10 + int(digits[-1:])

print(sum)
