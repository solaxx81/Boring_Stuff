# Ce programme dit Hello et demande mon nom.

print('Hello, world!')
print("Quel est ton nom?")  # Demande de mon nom.
mon_nom = input("> ")
print(f"C'est bon de te voir {mon_nom}")
print('La longueur de ton nom est : ')
print(len(mon_nom))
print('Quel est ton age : ')
mon_age=input("> ")
print(f"Tu seras agé de {int(mon_age)+1} dans un an.")
