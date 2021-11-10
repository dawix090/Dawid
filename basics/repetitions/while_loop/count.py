cables = int(input("How many live cables should I avoid?"))
number = int(1)
while number <= cables:
    print(f"Avoiding...Done! {number} live cables avoided")
    number += 1
print("All live cables have been avoided.")