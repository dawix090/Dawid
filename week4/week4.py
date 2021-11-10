print("Please enter a sequence: ")
seq = input()
print("please eneter the charcater for the marker: ")
mark = input()

m1 = 999999999
m2 = 99999999


for pos in range(len(seq)):
  let = seq[pos]
  if let == mark:
    if m1 == 999999999:
      m1 = pos
    elif m2 == 99999999 :
      m2 = pos

print(f"the distance between 2 markers is {m2-m1-1}")