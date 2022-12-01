with open('input') as inputFile:
  elves = inputFile.read().split('\n\n')
amounts = [sum(int(amount) for amount in elve.strip().split('\n'))
    for elve in elves]
print(sorted(amounts, reverse=True)[0])

print(sum(sorted(amounts, reverse=True)[0:3]))
