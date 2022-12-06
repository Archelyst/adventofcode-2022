with open('input') as inputFile:
  message = inputFile.read()

for i in range(3, len(message)):
  if len(set(message[i-3:i+1])) == 4:
    print(i+1)
    break

for i in range(13, len(message)):
  if len(set(message[i-13:i+1])) == 14:
    print(i+1)
    break
