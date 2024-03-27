dictionnaire_fr_ang = {'Bonjour': 'Hello', 'frere': 'brother', 'Oui': 'Yes' , 'maison':'house'}
def echange_cles_valeurs(dictionnaire):
    diction_inverse = {values: keys for keys, values in dictionnaire.items()}
    
    return diction_inverse

dictionnaire_ang_fr = echange_cles_valeurs(dictionnaire_fr_ang)
print("Dictionnaire Français/Anglais :", dictionnaire_fr_ang)
print("Dictionnaire Anglais/Français :", dictionnaire_ang_fr)
