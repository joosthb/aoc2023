import re

with open('1.txt', 'r') as fp:
  lines = fp.readlines()

pattern = r'[^0-9]'

sum = 0
for line in lines:
  digits = re.sub(pattern, '', line)
  sum += int(digits[:1])*10 + int(digits[-1:])
print(sum)