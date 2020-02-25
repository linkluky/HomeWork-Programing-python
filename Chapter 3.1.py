prompt = '-->'

print("Length of side 1:")
side1 = int(input(prompt))
print("Length of side 2")
side2 = int(input(prompt))
print("Length of side 3:")
side3 = int(input(prompt))
if side1 == side2 == side3: 
  print("All sides are equal, it's equilateral")
else:
  print("It's not equilateral")