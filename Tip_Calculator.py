#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


################### Code ####################

print("Welcome to the Tip calculator")

a = input(print("Enter the total bill"))
b = input(print("What percentage Tip you want to give"))
c = input(print("How many people to split the bill"))

total = float(a)
tip = float(b)
members = int(c)

var = tip / 100 * total + total
print(var)

