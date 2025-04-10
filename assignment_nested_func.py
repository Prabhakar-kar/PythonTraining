def counter():
    count = 0
    def inc():
        nonlocal count
        count = count+1
        return count
    return inc()
print(counter())