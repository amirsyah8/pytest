#name = "amie"
#age = 37
#gpa = 3.5a
#is_student = False

#print(f"my name is {name}")

#print(f"my nane is {name} and mu age is {age}")

#name = input("What is your name : ")
#age = input("your age : ")

#yearBirth = 2024-age

#print(f"Hello {name}")
#print(f"your birthday year is {yearBirth}")

#test 2

#length = float(input("Enter length: "))
#width = float(input("Enter width: "))

#area = length * width

#print(f"area is {area}cm²")
#item = None
#try:
#    item = int(input("What is like to buy: "))
#except ValueError:
#    print("yur input is error")
#if item is not None:
#    print(f"yur input is {item}")

while True:
    try:
        weight = float(input("Enter your weight : "))
        break
    except ValueError:
        print("Please enter a valid number for weight.")



unit = input("what is unit : ")

if unit == "k":
    weight = weight*2.205
    unit = "lbs"
    print(f"your weight is {weight} {unit}")
elif unit == "l":
    weight = weight/2.205
    unit = "kg"
    print(f"your weight is {weight} {unit}")
else:
    print("invalid unit")