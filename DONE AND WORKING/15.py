inp = input("Please enter a string, with spaces: ")
def find_longest_word(a_string):
    return max(len(word) for word in a_string.split())
print ("The longest word entered has a length of:")
print(find_longest_word(inp))
