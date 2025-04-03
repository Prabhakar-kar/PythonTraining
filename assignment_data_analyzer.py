def data_analyzer(numbers):
    if not numbers:
        return {
            "sum": 0,
            "min": None,
            "max": None,
            "average": None,
            "above_average_count": 0,
            "sorted_list": []
        }
    
    total_sum = sum(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    average = total_sum / len(numbers)
    above_average_count = sum(1 for num in numbers if num > average)
    sorted_list = sorted(numbers)
    
    return {
        "sum": total_sum,
        "min": min_value,
        "max": max_value,
        "average": average,
        "above_average_count": above_average_count,
        "sorted_list": sorted_list
    }

numbers = [10, 20, 30, 40, 50]
print(data_analyzer(numbers))
