def find_largest_smallest_word(text_string): 
    words = text_string.split()  # String to list of words

    if not words:
        return None

    smallest_word = words[0]
    largest_word = words[0]

    for word in words:
        if len(word) < len(smallest_word):
            smallest_word = word
        if len(word) > len(largest_word):
            largest_word = word

    return smallest_word, largest_word

input_string = "This is a string to find the largest and smallest words"
smallest, largest = find_largest_smallest_word(input_string)

if smallest is not None and largest is not None:
    print(f"The smallest word is: '{smallest}'")
    print(f"The largest word is: '{largest}'")
else:
    print("No words found in the string.")