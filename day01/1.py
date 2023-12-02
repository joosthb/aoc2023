"""Module providing a function parsing regex."""
import re

with open('1.txt', 'r', encoding="utf-8") as fp:
    lines = fp.readlines()

pattern = r'[^0-9]'
total = 0

for line in lines:
    digits = re.sub(pattern, '', line)
    total += int(digits[:1])*10 + int(digits[-1:])
print(total)
