inp = input("Enter a word you would like to evaluate: ")
def char_freq(str):
    freq = {}
    for c in str: #iterates over letters, because words are just lists 
        freq[c] = freq.get(c, 0) + 1 #Gets frequency of letters
    return freq

print(char_freq(inp))
