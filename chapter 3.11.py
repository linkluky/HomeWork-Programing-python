import random
prompt = '-->'

def playRound(budget: int) -> tuple:
    sum = sumOfDice(random.randint(1,6), random.randint(1,6))
    if sum == 7:
        budget += 4
        return ("Win",budget)
    else:
        budget -= 1
        return ("Loss",budget)

def sumOfDice(die1: int, die2: int) -> int:
        return die1 + die2

def haveMoney(budget: int) -> bool:
    return True if budget > 0 else False

def main():
    numRolls = 0
    outputString = "\t{0}\t\t{1}\t\t{2}"
    print("Gambeling Budget")
    budget = int(input(prompt))
    print("Number of rolls\t\tWin or Loss\tCurrent value of the pot")
    print(outputString.format(numRolls, "Put", budget))
    while haveMoney(budget):
        numRolls += 1
        output = playRound(budget)
        budget = output[1]
        print(outputString.format(numRolls, output[0], output[1]))

    print("Sorry you're out of money")    
    print("Heres your number of roles", numRolls)
if __name__ == "__main__":
    main()
