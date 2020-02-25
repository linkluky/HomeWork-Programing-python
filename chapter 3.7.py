prompt = '-->'
print("Start Salary")
startSalary = int(input(prompt))
print("Percent increase")
percentIncrease = (float(input(prompt)) / 100)
print("Years")
numberYears = list(range(1,(int(input(prompt)) + 1)))

for year in numberYears:
  salaryInc = startSalary*percentIncrease
  newSalary = startSalary+salaryInc
  startSalary = newSalary
  print("{} year salary is  {:0.2f}".format(year, newSalary))
