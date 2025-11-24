#--------------------Définition des fonctions--------------------#
#Fonction "turnOn" pour augmenter la luminosité d'une lumière de 1
def turnOn(x, y):
    grid[x][y] += 1

#Fonction "turnOff" pour baisser la luminosité d'une lumière de 1, sans descendre en dessous de 0
def turnOff(x, y):
    if grid[x][y] > 1:
        grid[x][y] -= 1
    else:
        grid[x][y] = 0

#Fonction "toggle" pour augmenter la luminosité d'une lumière de 2
def toggle(x, y):
    grid[x][y] += 2

#Fonction "instruction" pour traiter les commandes de l'utilisateur
def instruction():
    command = input("Entrez une commande :\nex: - 'turn on/off 0,0 through 999,999'\n    - 'toggle 0,0 through 999,999'\n")
    mots = command.split(" ")

    # La commande ressemblera toujours à "turn on/off/toggle" puis les premières coordonnées, puis through et enfin les secondes coordonnées
    # Donc on peut extraire les informations nécessaires en utilisant le découpage de chaîne
    # On extrait également l'action de la commande, qui peut être "turn on", "turn off" ou "toggle"

    coordinatesStart = mots[-3]
    coordinatesEnd = mots[-1]
    if mots[0] == "turn":
        action = mots[1]
    else:
        action = mots[0]

    # Ici on utilise la fonction map pour convertir les coordonnées extraites en entiers

    start1, start2 = map(int, coordinatesStart.split(","))
    end1, end2 = map(int, coordinatesEnd.split(","))
    # print("Coordonnées de début :", start1, start2)
    # print("Coordonnées de fin :", end1, end2)
    # print("Action :", action)

    # On parcourt la grille en fonction des coordonnées saisies et on applique l'action choisi par l'utilisateur
    for x in range(start1, end1 + 1):
        for y in range(start2, end2 + 1):
            if action == "on":
                turnOn(x, y)
            elif action == "off":
                turnOff(x, y)
            elif action == "toggle":
                toggle(x, y)

    return grid


#----------------------------Programme----------------------------#
# Création des variables pour la grille, le contrôle de la boucle et le compteur de lumières
grid = []
next = True
lightCount = 0

# Création de la matrice de 1000x1000 avec chaque lumière initialisée sur 0 (éteinte)
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    grid.append(row)

# Boucle principale pour exécuter les instructions jusqu'à ce que l'utilisateur décide d'arrêter

while next == True:
    grid = instruction()
    print(grid)
    answer = input("Voulez-vous continuer ? (Oui/Non) : ")
    if answer.lower() == "non":
        next = False
    else:
        next = True

# On peut maintenant compter le nombre de lumières allumées (valeur 1) dans la grille
for i in range(1000):
    for j in range(1000):
        if grid[i][j] != 0:
            lightCount += grid[i][j]

print("Nombre de lumières allumées :", lightCount)

#--------------------------Fin du programme------------------------#
# En suivant les instructions suivantes de la consigne :
# turn on 887,9 through 959,629
# turn on 454,398 through 844,448
# turn off 539,243 through 559,965
# turn off 370,819 through 676,868
# turn off 145,40 through 370,997
# turn off 301,3 through 808,453
# turn on 351,678 through 951,908
# toggle 720,196 through 897,994
# toggle 831,394 through 904,860
# Le résultat final de la partie 2 devrait être :
# Nombre de lumières allumées : 539 560