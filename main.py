# -*- coding: utf-8 -*-

height = 1.75
weight = 80.6

bmi = weight / (height ** 2)

print(bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")


    