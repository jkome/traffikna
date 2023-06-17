import numpy as np

# Paramètres du modèle
longueur_route = 50  # Longueur de la route en unités
nombre_vehicules = 20  # Nombre de véhicules sur la route
vitesse_maximale = 5  # Vitesse maximale des véhicules en unités de distance par étape de temps
distance_securite = 2  # Distance de sécurité entre les véhicules

# Création de la grille pour représenter la route
grille = np.zeros((longueur_route, ), dtype=int)

# Initialisation des positions et vitesses des véhicules de manière aléatoire
positions = np.random.choice(np.arange(longueur_route), size=nombre_vehicules, replace=False)
vitesses = np.random.randint(0, vitesse_maximale+1, size=nombre_vehicules)

# Fonction pour afficher l'état de la grille
def afficher_grille():
    for i in range(longueur_route):
        if i in positions:
            print("1", end=" ")  # Véhicule présent à cette position
        else:
            print("0", end=" ")  # Route vide à cette position
    print()

# Boucle de simulation
for etape in range(10):  # Simuler 10 étapes de temps
    print(f"Étape {etape + 1}:")
    afficher_grille()

    # Mise à jour des positions et vitesses des véhicules
    nouvelles_positions = []
    nouvelles_vitesses = []

    for i in range(nombre_vehicules):
        # Calcul de la position et de la vitesse du véhicule i+1
        position = positions[i]
        vitesse = vitesses[i]

        # Règles de déplacement basées sur la position des voisins
        distance_voisin_precedent = positions[i] - positions[i - 1] if i > 0 else longueur_route
        distance_voisin_suivant = positions[i + 1] - positions[i] if i < nombre_vehicules - 1 else longueur_route

        if distance_voisin_precedent <= vitesse:
            # Réduction de la vitesse pour maintenir une distance de sécurité
            vitesse = distance_voisin_precedent - 1

        if distance_voisin_suivant <= vitesse:
            # Réduction de la vitesse pour maintenir une distance de sécurité
            vitesse = distance_voisin_suivant - 1

        # Augmentation de la vitesse si elle est inférieure à la vitesse maximale
        vitesse = min(vitesse + 1, vitesse_maximale)

        # Calcul de la nouvelle position en fonction de la vitesse
        nouvelle_position = (position + vitesse) % longueur_route

        # Ajout des nouvelles positions et vitesses à la liste
        nouvelles_positions.append(nouvelle_position)
        nouvelles_vitesses.append(vitesse)

    # Mettre à jour les positions et vitesses pour l'étape de temps suivante
    positions = nouvelles_positions
    vitesses = nouvelles_vitesses

