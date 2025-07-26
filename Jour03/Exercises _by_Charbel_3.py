from math import*
# 1)
age = 19
# 2)
height = 1.88
# 3)
cube_root_of_one = complex(-0.5, (sqrt(3)/2))
# 4)
user_b = float(input("Enter base: "))
user_h = float(input("Enter height: "))
area_1 = 0.5*user_b*user_h
print(f"The area of the triangle is {area_1}")
# 5)
user_a = float(input("Enter side a: "))
user_b_1 = float(input("Enter side b: "))
user_c = float(input("Enter side c: "))
perimeter_1 = user_a + user_b_1 + user_c
print(f"The perimeter of the triangle is {perimeter_1}")
# 6)
user_l = float(input("Enter length: "))
user_w = float(input("Enter width: "))
area_2 = user_l*user_w
perimeter_2 = 2*(user_l + user_w)
# 7)
user_radius = float(input("Enter radius: "))
area_3 = pi*user_radius*user_radius
circumference = 2*pi*user_radius
# 8)
slope_1 = ((2*(0)-2)-(2*(1)-2))/(0-1)
# 9)
slope_2 = (10-2)/(6-2)
euclidian_distance = sqrt((2-6)**2 + (2-10)**2)
# 10)
print(slope_1 < slope_2)
# 11)
for x in range (-5,5,1):
    y = (x + 3)**2
    if (y == 0):
        print(y)
        print(f" y = 0 occurs for x = {x} ")
       
    else:
        print(y)
    
# 12)
print(len("python"))
print(len("dragon"))
print(len('python') != len('dragon'))  # → False
# 13)
print('on' in 'python' and 'on' in "dragon")
# 14)
print('jargon' in 'I hope this course is not full of jargon.')
# 15)
print("This statement is False")
# 16)
python_length = len('python')
print(python_length)
float_length_python = float(python_length)
str_length_python = str(python_length)
# 17)
# I test the parity of a integer by this prompt :
interger_number = int(input("Enter an interger: "))
if interger_number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
# 18)
cast_into_int = int(2.7)
floor_division = 7 // 3
print(floor_division == cast_into_int)
# 19)
print('10' is 10)
# 20)
print(int(9.8) == 10)
# 21)
user_hours = float(input("Enter hours: "))
user_rate_per_hour = float(input("Enter rate per hour: "))
user_pay = user_hours*user_rate_per_hour
print(f"Your weekly earning is {user_pay}")
# 22)
user_age_year = int(input("Enter number of years you have lived: "))
user_age_sec = user_age_year*365*24*3600
print(f"You have lived for {user_age_sec} seconds. ")
# 23)
for i in range(1,6,1):
    print(f"{i} {i**0} {i} {i**2} {i**3}")
