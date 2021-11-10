print("What type of adventure should I have?")
a = input()

if ((a.lower() == "short") or (a.lower() == "scary")):
  print("Entering the dark forest!")
elif ((a.lower() == "long") or (a.lower() == "safe")):
  print("Taking the safe route!")
else:
  print("Not sure which route to take.")