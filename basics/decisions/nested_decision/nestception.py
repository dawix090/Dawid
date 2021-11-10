options = 8

while options != 0:

  options =int(input("Where should I look \nChoose 1 for bedroom\n 2 for bathroom\n 3 for lab "))

  if options == 1:
    print("Where in the bedroom should I look ?")
    print("In the cupboard.")
    print("Found some mess but no battery")
    options == 8
  elif options == 2:
    print("Where in the bathroom should I look ?")
    print("In the bathtub")
    print("Found a rubber duck but no battery")
    options == 8
  elif options == 3:
    print("Where should I look?")
    print("In the lab!")
    print("Where in the lab should I look ?")
    print("Yes! I found my battery!")
    break

    