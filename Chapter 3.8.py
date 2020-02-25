prompt = '-->'

print("a is")
a = int(input(prompt))
print("b is")
b = int(input(prompt))

i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        gcd = i
    i = i + 1
    
print("gcd of the numbers is", gcd)