def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))
print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  
