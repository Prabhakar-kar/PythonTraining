pi = 3.14
e = 2.71
phi = 1.61

set_1 = {phi,2.5,e,4.5,5.5,pi,7.5}
set_2 = [pi,9.5,10.5,e,12.5,phi,14.5]


opr = input("Select method to do U/IN/DIF: ")

if opr == "U":
    res = set_1.union(set_2)
elif opr == "IN":
    res = set_1.intersection(set_2)
elif opr == "DIF":
    res = set_1.difference(set_2)    

print(res)