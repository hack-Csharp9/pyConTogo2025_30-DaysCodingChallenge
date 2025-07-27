from math import*

# 1)
space = ' '
concatenate_string_1 = 'Thirty' + space + 'Days' + space + 'Of' + space + 'Python'
print(concatenate_string_1)
# 2)
concatenate_string_2 = 'Coding' + space + 'For' + space + 'All'
print(concatenate_string_2)
# 3)
company =  "Coding For All"
# 4)
print(company)
# 5)
print(len(company))
# 6)
all_caps_company = company.upper()
print(all_caps_company)
# 7)
lowercase_company = all_caps_company.lower()
print(lowercase_company)
# 8)
capitalized_company = company.capitalize()
print(capitalized_company)

titled_company = company.title()
print(titled_company)

case_swapped_company = company.swapcase()
print(case_swapped_company)
# 9)
print(company[0:6])
# 10)
# first method
test = True
if company.index('Coding') == -1:
    print(f"The string contains 'Company' : {not test}")
else:
    print(f"The string contains 'Company' : {test}")
# second method
try:
    indice_Coding = company.index('Coding')
    print(f"Coding' was found in the string at the index : {indice_Coding}")
except ValueError:
    print("There is no 'Coding' in the string !")
# 11)
print(company.replace('Coding', 'Python')) 
# 12)
# first and last method 
string_var = "Python for Everyone"
string_var.replace('Everyone', 'All')
# 13)
print(company.split(' '))
# 14)
string_tech_team =  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string_tech_team.split(','))
# 15)
print(company[0])
# 16)
print(company[-1])
# 17)
print(company[10]) # Si vous ne voyer rien c'est le cactère espace
# 18)
string_name_1 = "Python For Everyone"
acronym_1 = string_name_1[0] + string_name_1[7] + string_name_1[11]
print(acronym_1)
# 19)
string_name_2 = "Coding For All"
acronym_2 = string_name_2[0] + string_name_2[7] + string_name_2[11]
print(acronym_2)
# 20)
print(company.index('C'))
# 21)
print(company.index('F'))
# 22)
people_company = company + ' People'
print(people_company)
print(people_company.rindex('i'))
# 23)
sentence_1 = "You cannot end a sentence with because because because is a conjunction"
print(sentence_1.index('because'))
# 24)
print(sentence_1.rindex('because'))
# 25)
print(sentence_1[31:54])
# 26)
sentence_1 = "You cannot end a sentence with because because because is a conjunction"
print(sentence_1.index('because'))
# 27)
print(sentence_1[31:54])
# 28)
print(company.index('Coding') == 0) # Yes
# 29)
print(company.index('Coding') == len(company)) # False
# 30)
test_space_company = "   Coding For All      "
print(test_space_company.strip(' '))
# 31)
challenge_1 = "30DaysOfPython"
challenge_2 = "thirty_days_of_python"
print(challenge_1.isidentifier())
print(challenge_2.isidentifier()) # this is true
# 32)
list_test =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(list_test)
print(result)
# 33)
print("I am enjoying this challenge.\nI just wonder what is next.")
# 34)
# Use \t to create tabs for column alignment
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")
# 35)
radius = 10
area = 3.14 * radius ** 2

# Method 1: Using f-strings (recommended)
print(f"radius = {radius}")
print(f"area = 3.14 * radius ** 2")
print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")

print()  # Empty line for separation

# Method 2: Using .format() method
print("radius = {}".format(radius))
print("area = 3.14 * radius ** 2")
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

print()  # Empty line for separation

# Method 3: Using % formatting (older style)
print("radius = %d" % radius)
print("area = 3.14 * radius ** 2")
print("The area of a circle with radius %d is %.0f meters square." % (radius, area))
# 36)
a = 8
b = 6

# Calculate all operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor_division = a // b
exponentiation = a ** b

# Method 1: Using f-strings
print("Using f-strings:")
print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {subtraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{a} / {b} = {division:.2f}")
print(f"{a} % {b} = {modulus}")
print(f"{a} // {b} = {floor_division}")
print(f"{a} ** {b} = {exponentiation}")

print()  # Empty line for separation

# Method 2: Using .format() method
print("Using .format() method:")
print("{} + {} = {}".format(a, b, addition))
print("{} - {} = {}".format(a, b, subtraction))
print("{} * {} = {}".format(a, b, multiplication))
print("{} / {} = {:.2f}".format(a, b, division))
print("{} % {} = {}".format(a, b, modulus))
print("{} // {} = {}".format(a, b, floor_division))
print("{} ** {} = {}".format(a, b, exponentiation))

print()  # Empty line for separation

# Method 3: Using % formatting
print("Using % formatting:")
print("%d + %d = %d" % (a, b, addition))
print("%d - %d = %d" % (a, b, subtraction))
print("%d * %d = %d" % (a, b, multiplication))
print("%d / %d = %.2f" % (a, b, division))
print("%d %% %d = %d" % (a, b, modulus))  # Note: %% to display literal %
print("%d // %d = %d" % (a, b, floor_division))
print("%d ** %d = %d" % (a, b, exponentiation))