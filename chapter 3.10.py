prompt = '-->'
ANNUAL_INTEREST = 0.12
MONTHLY_RATE = 0.12/12

print("Purchase Price")
Price = int(input(prompt))
downPayment = Price * .1
originalBalance = Price - downPayment
payment = originalBalance * 0.05
print("Month", "Orig. Bal.", "Monthly Interest", "Principal", "Payment", "New Bal.")

month = 0
while originalBalance > payment:
	month += 1
	interest = originalBalance * MONTHLY_RATE
	principal = payment - interest
	newBalance = originalBalance - principal
	print("%-1d%10.2f%12.2f%12.2f%7.2f%9.2f" % (month, originalBalance, interest, principal, payment, newBalance))
	originalBalance = newBalance	
	
payment=originalBalance
interest=0
principal=payment
month = month+1
newBalance=0
print("%-1d%10.2f%12.2f%12.2f%7.2f%9.2f" % (month, originalBalance, interest, principal, payment, newBalance))