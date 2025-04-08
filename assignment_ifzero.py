def if_zero(num):
    for n in num:
        if n == 0:
            return False
        print(n)

print(if_zero([1, 2, 5, 0, 7, 8]))