#Division By Zero Error
a = 1 / 0
print(a)

#Value Error
a = 34
b = "CodeWithArhan"
 
#works normally 
print(float(a))
 
#leads to the valueerror
print(float(b))

#Type Error
name = "Arhan"
num = 4
print(name + num + name)

#Index Error
j = [1, 2, 4]
print(j[4])

my_string = "CodeWithArhan"
print(my_string[-61])

#Try Except Block
try:
 x = 1/0
except:
 print("Division By Zero")

#Else and Finally Block
try:
 y = 1/1
except ZeroDivisionError:
 print("You can't divide by zero!")
else:
 print("No exceptions were raised")
finally:
 print("This block runs no matter what.")

#Custom Exceptions

class MyError(Exception):
 pass

try:
 raise MyError("Something went wrong!")
except MyError as e:
 print(e)
