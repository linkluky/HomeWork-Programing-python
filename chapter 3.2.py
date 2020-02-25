prompt = '-->'

print("Length of side 1:")
a = int(input(prompt))
print("Length of side 2")
b = int(input(prompt))
print("Length of side 3:")
c = int(input(prompt)) 
if (a^2 + b^2) == c^2: #Determines if it's a right triangle
  print("It's a right triangle")
else:
  print("It's not a right triangle")