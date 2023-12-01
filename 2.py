import re

transtable = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

with open('1.txt', 'r') as fp:
  lines = fp.readlines()

pattern = r'[^0-9]'

sum = 0
for line in lines:
  for number in transtable:
    line = line.replace(number, number + transtable[number] + number )
  digits = re.sub(pattern, '', line)
  sum += int(digits[:1])*10 + int(digits[-1:])
print(sum)