def crypter_mc(x):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for lettre in x:
        oc = x.count(lettre)
        pos = 0
        if oc % 2 == 0:
            pos = oc // 2 
        else:
            pos = oc * 2
        ordre = alpha.find(lettre)
        indice = (pos + ordre) % 26  
        res += alpha[indice]
    return res

x = input('entrer un chain cara : ')
print(crypter_mc('x'))
