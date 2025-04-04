from functools import reduce

longest_word = lambda words: reduce(lambda a, b: a if len(a) >= len(b) else b, words)

words_list = ["apple", "banana", "cherry", "blueberry", "kiwi"]
print(longest_word(words_list))  
