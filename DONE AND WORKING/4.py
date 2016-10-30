"""Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""
original = raw_input('Enter a letter: ')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if first in ('a', 'e', 'i', 'o', 'u'):
        print ("vowel")
    else:
        print ("consonant")
else:
    print ("empty")
