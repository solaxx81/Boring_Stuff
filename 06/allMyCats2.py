noms_chats = []
while True:
    print(f"Entrer le nom du chat {len(noms_chats) + 1} ou rien pour arrêter.")
    nom = input()
    if nom == "":
        break
    noms_chats = noms_chats + [nom]
print("Les noms des chats sont :")
for nom in noms_chats:
    print(f" - {nom}")
