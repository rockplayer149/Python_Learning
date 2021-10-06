# #You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

#another way to solve.
total2 = 0
for number in range(1,101):
    if number %2 == 0:
        total2 += number
print(total2)