with open('input') as inputFile:
  elves = inputFile.read().split('\n\n')
amounts = [
  sum(int(amount)
  for amount in elve.strip().split('\n'))
  for elve in elves]

print(sorted(amounts)[-1])
print(sum(sorted(amounts)[-3:]))
