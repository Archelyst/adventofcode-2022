import string

with open('input') as inputFile:
  rucksacks = [line.strip() for line in inputFile]

total = 0
for rucksack in rucksacks:
  mid = len(rucksack) // 2
  common = (set(rucksack[:mid]) & set(rucksack[mid:])).pop()
  total += ord(common) - (96 if common.lower() == common else 38)
print(total)


total2 = 0
for i in range(0, len(rucksacks), 3):
  r1 = set(rucksacks[i])
  r2 = set(rucksacks[i+1])
  r3 = set(rucksacks[i+2])
  common = (r1 & r2 & r3).pop()
  total2 += ord(common) - (96 if common.lower() == common else 38)
print(total2)
