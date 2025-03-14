input_string = input("Enter comma-separated words: ")

sorted_words = ','.join([word for word in sorted(input_string.split(','))])

print(sorted_words)