prompt = '-->'
print("Inital Organism")
organisms = int(input(prompt))
print("Rate of growth?")
rateOfGrowth = int(input(prompt))
print("number of hours?")
numOfhours = int(input(prompt))
print("total hours?")
totalhours = int(input(prompt))
hours=0
while (hours <= totalhours):
    organisms*=rateOfGrowth
    hours += numOfhours
    if (hours==totalhours):
        break
print("The total population:" ,organisms)
