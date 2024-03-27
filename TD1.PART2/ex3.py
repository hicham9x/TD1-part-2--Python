import string
letters = string.ascii_letters
chainCara = input('entrer une chain cara :')
decal = int(input('enrer un decalage :'))
chainCara = list(chainCara)
for i,v in enumerate(chainCara):
   chainCara[i] = letters[letters.index(v) + decal]
print(''.join(chainCara).upper())