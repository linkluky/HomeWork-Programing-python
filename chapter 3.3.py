import random
import math
prompt = '-->'

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
print("number")
number = int(input(prompt))
count = 0
if smaller == larger:
    print ("Cheater")
    exit()
if number > larger:
    print ("Cheater")
    exit()
if number < smaller:
    print ("Cheater")
    exit()
comNumber = random.randint(smaller, larger)
while True: 
  count += 1 
  print ("your number is",comNumber)
  print("<,>,=")
  Answer = (input(prompt))
  if Answer == "=":
    print ("You got it in",count)
    break
  elif Answer == "<":
    comNumber = comNumber -1
  else:
    comNumber = comNumber + 1
