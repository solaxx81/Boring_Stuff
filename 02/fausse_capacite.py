# Calculateur capacité réelle de stockage - chapitre 2 p.45

print("Entrer l'unité de stockage utilisée (Go ou To) :")
unite: str = input("> ")
perte = 0

if unite.lower() == "to":
    perte = 1000000000000 / 1099511627776
elif unite.lower() == "go":
    perte = 1000000000 / 1073741824

print("Entrer la capacité affichée de l'unité de stockage :")
capacite = float(input("> "))

capacite_reelle = round(capacite * perte, 2)

print(f"La capacité réelle est {capacite_reelle} {unite}")
