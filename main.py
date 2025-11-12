# Création de la matrice de 1000x1000 avec chaque lumière initialisée sur 0 (éteinte)
grid = []

for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    grid.append(row)

command = input("Entrez une commande :\nex: - 'turn on/off 0,0 through 999,999'\n    - 'toggle 0,0 through 999,999'\n")
mots = command.split("")

# La commande ressemblera toujours à "turn on/off/toggle" puis les premières coordonnées, puis through et enfin les secondes coordonnées
# Donc on peut extraire les informations nécessaires en utilisant le découpage de chaîne

coordinatesStart = mots[-3]
coordinatesEnd = mots[-1]
if mots[0] == "turn":
    action = mots[1]
else:
    action = mots[0]

# On extrait également l'action de la commande, qui peut être "turn on", "turn off" ou "toggle"

start1, start2 = map(int, coordinatesStart.split(","))
end1, end2 = map(int, coordinatesEnd.split(","))

# Ici on utilise la fonction map pour convertir les coordonnées extraites en entiers

# print(grid)