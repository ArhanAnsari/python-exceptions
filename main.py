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
