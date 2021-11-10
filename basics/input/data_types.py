#print("What is your name human?")
#name = input()
#print("It is nice to meet you human " + name +".")

# alternative way of the above string
#print("Nice to meet you {}.".format(name))


#body mass index calculaton below
print("what is your name?")
name = input()
print("how old are you?")
age = int(input())
print("how tall are you(in meters)?")
height = float(input())
print("how much do you weight(in kilograms)")
weight = int(input())
print (name) 
print("you are") 
print(age) 
print("years old and your bmi is")
number = weight / height**2  
print (number)