# name = len(input("Enter your name"))
# print("Your name contains" + name + "characters")

#by doing so we will get type error
# Because we adding string with integer , so we need to convert it into a string


######## Code ###########

name = len(input("Enter your name \n"))
new_name = str(name)
print("Your name contains " +  new_name  + " characters")

################################

print(70 + float("1200.3"))