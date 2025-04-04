power = lambda n: lambda x: x**n
n = int(input("Enter n value: "))

caLc = power(n)
x = int(input("Enter x value: "))

print(caLc(x))