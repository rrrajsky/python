
height = 0
while 0 >= height:
    try:
        height = int(input("your height: \n"))
    except ValueError:
        print("please enter a valid number")

weight = 0
while 0 >= weight:
    try:
        weight = int(input("your weight: \n"))
    except ValueError:
        print("please enter a valid number")

bmi = weight/pow(height,2)

print("your BMI is", bmi)

if bmi < 18.5:
    print("you are underweight")
elif bmi < 25.0:
    print("you are normal")
elif bmi < 30.0:
    print("you are overweight")
elif bmi < 40.0:
    print("you are obese")
else:
   print("you are morbidly obese")