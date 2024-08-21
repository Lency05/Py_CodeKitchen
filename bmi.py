height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kg:"))
#formula to calculate BMI
bmi = weight / (height ** 2)
print("Your BMI is {0} and you are".format(bmi))
#Conditions
if bmi < 16:
 print("Severely underweight")
elif 16 <= bmi < 18.5:
 print("Underweight")
elif 18.5 <= bmi < 25:
 print("Healthy")
elif 25 <= bmi < 30:
 print("Overweight")
elif bmi >= 30:
 print("Severely Overweight")



