#Golbal Variables
#Golbal variables can be used from anywhere inside as well as outside
#Create a variable outside of a function, and use it inside the function
x = "Riju"
def functiom():
    print(x +" " "is a good boy.")

functiom()

#######################################

"""Create a variable inside a function, with the same name as the global variable"""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)