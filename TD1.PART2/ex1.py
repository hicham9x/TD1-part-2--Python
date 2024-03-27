import string
letters = string.ascii_letters
chainCara = input('entrer une chain cara :').lower()
chainCara = list(chainCara)
for i,lett in enumerate(chainCara):
   chainCara[i] = letters[letters.index(lett) + 1]
print(''.join(chainCara))