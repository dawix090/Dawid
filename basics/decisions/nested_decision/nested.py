cover = input("What type of cover does the book have ? \n")
#bound = input("Is the book perfect-bound ? \n")
if cover.lower() == "soft":
  bound = input("is the book perfect bound? \n")
  if bound.lower() == "yes":
# and bound.lower() == "yes":
   print("Soft cover,perfect bound books are very popular.")
  elif  bound.lower() == "no":
    print("Soft covers with coils or stitches are great for short books.") 
else:
  print("Books with hard covers can be expensive!")