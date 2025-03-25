#Clothing advisor for different weathers

temp = int(input("Enter temperature in celcius: "))

if temp < 10:
    print("It's cold outside wear a sweater!")
elif temp >= 10 and temp <= 25:
    print("It's a mild weather wear a light jacket!")
elif temp > 25:
    print("It's hot outside wear something light!")

else:
    print("Enter proper temperature!")