import numpy

temp = input('Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F): ')

if temp == "C":
    C = int(input('Enter temp in celsius: '))
    Conversion_C2F = round(C*(9/5)+32) # Celsius to fahrenheit conversion formula 
    print(Conversion_C2F, end="F")
elif temp == "F":
    F = int(input('Enter temp in fahrenheit: '))
    Conversion_F2C = round((F-32)*(5/9)) # Fahrenheit to celsius conversion formula
    print(Conversion_F2C, end='C')
else:
    print("Enter correctly!")