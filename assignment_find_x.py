def find_x(s):
    pos = -1
    for i in range(len(s)):
        if s[i] == 'x':
            pos = i
            break
    return pos
print(find_x("The experimental xenon exhaust extractor exceeded expectations in extreme x-ray exposure experiments"))