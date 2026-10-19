#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
height = int(input("enter your height in meters (make sure to round to whole number): "))
weight = int(input("enter your weight in kilograms (make sure to round to whole number): "))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("you are underweight")
elif BMI < 25:
    print("you are normal weight")
elif BMI < 30:
    print("you are overweight")
else:
    print("you are obese")
