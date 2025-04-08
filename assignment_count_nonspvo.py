def count_non_spvo(s):
    count = 0 
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            continue
        if char != ' ':
            count += 1
    return count
print(count_non_spvo("The way to succeed is to double your failure rate"))
