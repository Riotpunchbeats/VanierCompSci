rob = raw_input("please enter a sting you would like translated: ")
def translate(s):
  consonants = 'bcdfghjklmnpqrstvwxz'
  return ''.join(l + 'o' + l if l in consonants else l for l in s)

print(translate(rob))
