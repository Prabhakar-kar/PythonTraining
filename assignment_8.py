myList = []   #Creating an empty list

for number in range(201):  #For loop 
    if number % 2 == 0:   #Condition checking for even numbers
        myList.append(number)  #Adding the elements to the list
print(myList)