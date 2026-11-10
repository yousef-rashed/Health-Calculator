# start of the app and inputs
print(" Welcome to the Health app." )
name = input("please enter your name: ")
print ( "Hello " + name )
print("Please answer the following questions so that the app can function accurately.")
while True:
    try:
        weight = float(input("Please enter your weight by Kg: "))
        height = float(input("Please enter your height by cm: "))
        age = float(input("Please enter your age: "))
        break
    except(ValueError):
        print("please enter a numbers only")
        continue
while True:
    sex = input("Please enter your sex: ").lower()
    if sex == "male" or sex == "m" or sex == "female" or sex == "f":
        break
    else:
        print("please enter your sex: (male or female)")
print("""Do you exercise?
1. Every day.
2. Sometimes.
3. I do not exercise.""")
while True:
    doing_sports = input("Please enter the appropriate number:")
    if doing_sports == "1" or doing_sports == "2" or doing_sports == "3":
        break
    else:
        print("please enter a number from 1, 2 or 3")

def main():
    # BMI
    def BMI():
        height_by_meter = height / 100
        height_squared = height_by_meter ** 2
        result_of_BMI = weight / height_squared
        return(result_of_BMI)

    # Calorie counting
    def calorie_counting():
        frist = weight * 10
        scound = height * 6.25
        thried = age * 5
        total = frist + scound - thried
        if sex == "male" or sex == "m":
            total = total + 5
        else:
            total = total - 161
        result_of_calorie_counting = total
        return(result_of_calorie_counting)

    # Adding motion effort
    def adding_motion_effort():   
        if doing_sports == "1":
            final_caories = calorie_counting() * 1.725
        elif doing_sports == "2":
            final_caories = calorie_counting() * 1.55
        else:
            final_caories = calorie_counting() * 1.2
        result_of_adding_motion_effort = final_caories
        return(result_of_adding_motion_effort)
    
    bmi = BMI()
    Adding_motion_effort = adding_motion_effort()

    print(f"your BMI is {round(bmi, 2)}")
    if  bmi < 18.5:
        print("You are underweight and need to gain weight.")
    elif 18.5 <= bmi <= 24.9:
        print("Your weight is ideal.")
    elif 25 <= bmi <= 29.9:
        print("You have some excess weight and need to lose a little.")
    else:
        print("You are morbidly obese; you need to lose weight seriously.")
    print(f"You need {Adding_motion_effort} calorie per day.")
main()