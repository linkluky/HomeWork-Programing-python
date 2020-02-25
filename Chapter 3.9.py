prompt = '-->'
numbers = []
count = 0


while True: 
    print("Press enter")
    data = input(prompt)
    if data == "":
        break
    numbers.append(float(data))

count = len(numbers)
if count > 0:
    _sum = sum(numbers)
    average = _sum / float(count)

    print("The sum is", _sum)
    print("The average is", average)
else:
    print("Nothing was entered")