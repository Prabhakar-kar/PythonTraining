currency = input("Choose your currency USD/POUND/YEN/EURO/RUBLE: ")

if currency == "USD":
    amount_usd = int(input("Enter amount: "))
    to_inr = amount_usd * 86.62
elif currency == "POUND":
    amount_pound = int(input("Enter amount: "))
    to_inr = amount_pound * 112.57
elif currency == "YEN":
    amount_yen = int(input("Enter amount: "))
    to_inr = amount_yen * 0.58
elif currency == "EURO":
    amount_euro = int(input("Enter amount: "))
    to_inr = amount_euro * 94.73
elif currency == "RUBLE":
    amount_ruble = int(input("Enter amount: "))
    to_inr = amount_ruble * 1.06

else:
    print("Choose from these only")
print(f"{currency} to INR is {round(to_inr)}")