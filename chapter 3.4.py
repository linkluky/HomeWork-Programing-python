prompt = '-->'
distance = 0

print("height?")
height = float(input(prompt))
print("Bouncines?")
Bouncy = int(input(prompt))
print("bounce?")
bounce = int(input(prompt))

while bounce >  0:
  height = height * Bouncy
  distance = distance + height
  bounce -= 1
print("total distance",distance)