def dimension():
  l = float(input("Enter lenght of the room:"))
  w = float(input("Enter the wight of the room:"))
  return l,w #Returnig a tuple of two values together

def calc_area(l,w):
  return l*w
def name_room():
  return input("Enter the name of the room: ")

def price(name,area):
  if name.lower() == "bedroom":
    return 20*area
  elif name.lower() == "bathroom":
    return 12*area
  elif name.lower() == "kitchen":
    return 15*area
  else:
     return 55*area
def run():
  total_price = 0.0
  num = int(input("how many room would you like to paint?"))
  for i in range(num):
    n = name_room()
    lenght,width = dimension()
    area = calc_area(lenght,width)
    x = price(n,area)
    total_price += x
  print(f"The total price of the job is £{total_price}")
run()