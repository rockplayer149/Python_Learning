# Data Types
# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# Example Input
# 39
# Example Output
# 3 + 9 = 12

# 12
# e.g. When you hit run, this is what should happen:

# Hint
# Try to find out the data type of two_digit_number.
# Think about what you learnt about subscripting.
# Think about type conversion.

######################################################

num = input(print("Enter a number"))
a = num[0]
b = num[1]
print(int(a) + int(b))