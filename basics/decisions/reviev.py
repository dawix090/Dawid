#Decisions with if...elif...else statements
#- Nested decisions
#- Multiple conditions with logical (AND, OR and NOT) operators


obj =input("What is that object? (chose: ball or yo-yo or pen\n")
col =input(f"What color is that {obj}?(chose: red or blue)\n")

if ((obj.lower() =="ball") or (obj.lower() == "yo-yo") and(col.lower() =="red")):
  print(f"Beep likes circular red objects such as this{obj}")

elif ((obj.lower() =="pen")) and ((col.lower() == "blue")) or ((col.lower() == "red")):
  print(f"This pen is colored {col} and beep thinks it will write in {col} as well.")

else:
  print("Beep doesn't like this object but will use it anyway :>")
