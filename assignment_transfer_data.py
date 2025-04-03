def transform_data(numbers):
    filtered_numbers = filter(lambda x: x >= 0, numbers)
    squared_numbers = map(lambda x: x ** 2, filtered_numbers)
    product = 1
    for num in squared_numbers:
        product *= num
    
    return product

numbers = [-3, 4, -2, 5, 6]
result = transform_data(numbers)
print(result)  
