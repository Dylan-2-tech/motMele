
"""
import string

def ascii_in(mot):

	correct = True
	indc = 0

	while correct and indc < len(mot):
		correct = mot[indc] in string.ascii_lowercase or "\n" in mot[indc]
		indc += 1

	return correct


# nettoyage des mots
with open('../mot/liste_francais.txt', "r+", encoding = "latin-1") as f:
	words = [word.lower() for word in f if len(word) < 11 and len(word) > 5] # Entre 4 et 9 pck \n vaut 1 
	words = [word for word in words if ascii_in(word)]
f.close()


with open('../mot/liste_mots.txt', 'w') as f:
	f.writelines(words)
"""


def affichage_grille(g):

	for listeLettre in grille:
		print(listeLettre)
	print()

grille = [["" for i in range(9)] for i in range(9)]
liste_mot = ["manger","siffler","caillou"]

grille[3][6] = 'T'
affichage_grille(grille)

#### Fonctions qui placent le mot dans la grille de 4 manière différentes ####
# Fonction qui place un mot donner à la verticale
def search_vert(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if y < len(grille) and grille[y][x] == "":
			liste_positions.append((x,y))
			indC += 1
			y += 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True
# Fonction qui place un mot donner à l'horizontale
def search_hori(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x < len(grille[0]) and grille[y][x] == "":
			liste_positions.append((x,y))
			indC += 1
			x += 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True
# Fonction qui place un mot donner en diagonale de gauche à droite
def search_diag_gd(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x < len(grille[0]) and y < len(grille) and grille[y][x] == "":
			liste_positions.append((x,y))
			indC += 1
			y += 1
			x += 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True
# Fonction qui place un mot donner en diagonale de droite à gauche
def search_diag_dg(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x >= 0 and y < len(grille) and grille[y][x] == "":
			liste_positions.append((x,y))
			indC += 1
			y += 1
			x -= 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True

# Fonction pour placer les lettres du mot au positions voulu
def placer_mot(mot, liste_positions):
	# On parcours les position et on place chaque lettre du mot
	print(liste_positions)

	for i in range(len(liste_positions)):
		# Récupération des positions
		x = liste_positions[i][0]
		y = liste_positions[i][1]

		# Affectation des lettres du mot dans les cases vides de la grille
		grille[y][x] = mot[i]

print(search_diag_gd("manger", 0, 3))
print(search_vert("voir", 5, 4))
affichage_grille(grille)

'''
REVERSE D'UNE CHAINE DE CARACTERE: [::-1]
'''