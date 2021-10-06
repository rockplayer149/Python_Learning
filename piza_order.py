# Pizza Order
# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
# e.g. When you hit run, this is what should happen:

# Hint
# Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    print("Your Pizza size is small")
    bill = 15
    print("price will be $15")
elif size == "M":
    bill = 20
    print("price will be $15")
else:
    bill = 25
    print("price will be $15")

if add_pepperoni == "y":
    if size == "S":
        bill += 2
    else:
      bill += 3

if extra_cheese == "y":
    bill += 1
    print(f"your final bill is ${bill}")