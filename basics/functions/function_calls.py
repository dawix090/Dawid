def display(w):
  l = len(w)
  print("="*(l+2))
  print("="+ w + "=")
  print("="*(l+2))

def display_low(w):
  return w.lower()
  
def display_up(w):
  return w.upper()

def mirror(w):
  print(f"{w}  |  {w[::-1]}")

def repeat(w):
  print("how many times would you like to repeat the word ?")
  n = int(input())
  for i in range(n):
    if i%2 == 1:
      print(w.upper())
    else:
      print(w.lower())


def run():
  w = input("What is the word you would like to play with?")
  print("Choose 1 item from the menu:\n\n1-Display in a box\n2-Lower case\n3-Upper case\n4-Display mirrored\n5-Repeat")
  response =int(input())
  if response ==1:
    display(w)
  elif response ==2:
    print(display_low(w))
  elif response == 3:
    print(display_up(w))
  elif response == 4:
    mirror(w)
  elif response == 5:
    repeat(w)

run()