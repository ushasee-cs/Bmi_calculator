

print("Welcome to the BMI calculator!")
Permission = (input("Do You want to check your BMI?"))
if Permission == "Yes":
    print("OK, lets go through the bellow processes")
    Weight = int(input("Enter your weight in kg"))
    Height = float(input("Enter your height in m"))
    bmi = Weight / (Height ** 2)
    if bmi < 18.5:
        print("You are underweight!")
    elif bmi == 18.5:
        print("You are normal!")
    elif bmi < 25:
        print("You are normal!")
    else:
        print("You are overweight!")
else:
    print("Its OK, its your choice\nHave a nice day ahead!")




