#simple function definition to calculate an area of a trianangle
def calc_area(h,b):

  area = 0.5*h*b
  print(area)
#call to the function
#for i in range (5):
  #calc_area()


height = float(input("Enter the height of the trianangle")) 
base = float(input("Enter the base of the triangle"))

calc_area(5,7)
calc_area(height,base)
calc_area(8, 9.3)