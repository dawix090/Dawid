options = 8

while options != 0:
  #while True:


  print("Please choose one of the following options:\n \n1-Nice message\n2-Area of a rectangle \n3-Area of a trianagle \n4-Times table \n0-Exit ")

  options = int(input())

  if options == 1:
    print("You do not smell so bad today!")
  elif options == 2:
    w = float(input("enter the width of a rectnagle:"))
    l = float(input("enter the lenght of a rectangle"))
    area =w*l
    print("The area is {}".format(area))
  elif options == 3:
    l=float(input("Enter the length of the trainagle:"))
    h=float(input("enter the height of the traiangle"))
    area = h*l/2
    print("The area is {}".format(area))
  elif options == 4:
    n = int(input("Enter a whole number:  "))
    for i in range(1, 11, 1):
      print(f"{i}x{n} = {i*n}")
  elif options == 0:
    break
  else:
    print("whoops wrong number buddy :> .")