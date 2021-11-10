a = int(input("Enter your 1st whole number: "))
b = int(input("Enter your 2nd whole number: "))
c = int(input("Enter your 3rd whole number: "))

if ((a % 2 != 0) and ((b % 2 != 0) and (c % 2 != 0))):
  print("There were 3 odd numbers and 0 even numbers")
elif(a % 2 == 0, b % 2 != 0, c % 2 !=0):
  print("There were 2 odd number and 1 even numbers")
elif (a % 2 != 0, b % 2 == 0, c % 2 !=0):
  print("There were 2 odd number and 1 even numbers")
elif(a % 2 != 0, b % 2 != 0, c % 2 ==0):
  print("There were 2 odd number and 1 even numbers")
elif(a % 2 == 0, b % 2 == 0, c % 2 !=0):
  print("There were 1 odd number and 2 even numbers")
elif(a % 2 == 0, b % 2 != 0, c % 2 ==0):
  print("There were 1 odd number and 2 even numbers")
elif(a % 2 != 0, b % 2 == 0, c % 2 ==0):
  print("There were 1 odd number and 2 even numbers")
elif(a % 2 == 0, b % 2 == 0, c % 2 ==0):
  print("There were 0 odd number and 3 even numbers")