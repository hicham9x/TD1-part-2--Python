import random 
 
nbr_v_at = int(input("donner un nomber a tire au hasard :") or 1000)
frac = int(input("donner fractions partager linter val possible de 0 à 1 :") or 5)
frac = max(2, min(frac,nbr_v_at// 10))
compteurs = [0] * frac
val_tire = [random.random() for i in range(nbr_v_at)]

for valeur in val_tire:
    fraction = int(valeur * frac)
    compteurs[fraction] += 1
print("État des compteurs :", compteurs)