def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a  
    elif b >= a and b >= c:
        return b  
    else:
        return c  

print(max_of_three(2, 14, 7))  
