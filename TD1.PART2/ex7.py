def remplissage():
    my_dict = {}
    nbr_cop = int(input("donner le nombre de copain :"))
    for i in range(nbr_cop):
             nom = str(input(f'donner nom de  {i+1} copain :'))
             age = int(input('donner  age :'))
             taille = input('donner taille :')
            
             my_dict[nom] = (age,taille)
    return my_dict
my_dict = remplissage()
def rechercheDict(diction):
    while True :
        recherchName = input("entrer le nom de copaine ou exit pour quitter ")
        if recherchName.lower() == 'exit' :
            break
        if recherchName in my_dict :
            age , taille = diction[recherchName]
            res = "Nom :{}  - age :{} ans  - taille :{} ".format(recherchName,age,taille)
            print(res)
        else :
            print('this name does not in your dict')
rechercheDict(my_dict)


