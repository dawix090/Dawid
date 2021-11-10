salary = float(input("Enter your Salary: "))
years = int(input("How long are you with the company? "))

  if years > 2:
    if salary < 25000:
      salary = salary *1.1
      #salary *=1.1 does the same thing
      print(f"your new salary is now {salary})
    else:
      salary+=100
      print(f"your new salary is now {salary})
  elif years > 1:
    print("No salary increase for you!")
  else:
    if salary <15000
    print("apologies, this was an error. You shall earn 20000")
    salary = 20000
  print("let us work for the good of the corporation")
#nested = an if statment in a if statement