num = [1,2,3,4,5,6,7,8,9,10,11,12,13]

even_count = len([n for n in num if n%2==0])
odd_count = len(num)-even_count

print(even_count)
print(odd_count)