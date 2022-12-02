points = {'X': 1, 'Y': 2, 'Z': 3}
beats = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draws = {'A': 'X', 'B': 'Y', 'C': 'Z'}
loses = {'A': 'Z', 'B': 'X', 'C': 'Y'}

def getPoints(rounds):
  return sum([
    (6 if beats[runde[0]] == runde[1] else 0) +
    (3 if draws[runde[0]] == runde[1] else 0) +
    points[runde[1]]
    for runde in rounds])


with open('input') as inputFile:
  rounds = [line.strip().split() for line in inputFile]
print(getPoints(rounds))

def getShape(opponentsShape, outcome):
  if outcome == 'Z':
    return beats[opponentsShape]
  if outcome == 'Y':
    return draws[opponentsShape]
  return loses[opponentsShape]

print(getPoints([(runde[0], getShape(runde[0], runde[1])) for runde in rounds]))
