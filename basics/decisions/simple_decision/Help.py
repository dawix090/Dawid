number1 = int(input("Enter number and hit enter "))
number2 = int(input("Enter number and hit enter "))
number3 = int(input("Enter number and hit enter "))

list1 = [number1, number2, number3]

even_count, odd_count = 0, 0

for num in list1:

    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers: ", even_count)
print("Odd numbers: ", odd_count)