def check_prime(num):
    if num == 0 or num == 1:
        return "Not a prime"
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "Not a prime"
        else:
            return "Is a prime"
print(check_prime(2))