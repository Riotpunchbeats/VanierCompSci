
def map_to_lengths_for(words): #For loop that does the same as higher order function map()
    lengths = [] #Initialize list to hold word lengths
    for word in words:
        lengths.append(len(word)) #Appends word length to list
    return lengths

def map_to_lengths_map(words): #MAP NO LONGER WORKS LIKE THIS IN PYTHON 3.X
    return map(len, words)

def map_to_lengths_lists(words): #same thing, this time using list comprehesion
    return [len(word) for word in words] #iterates over word list and returns len

words = raw_input("enter some words with a space: ").split()

print (map_to_lengths_for(words))
print (map_to_lengths_map(words))
print (map_to_lengths_lists(words))
