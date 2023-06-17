import pygame
import numpy as np

# Paramètres du modèle
longueur_route = 50  # Longueur de la route en unités
nombre_vehicules = 20  # Nombre de véhicules sur la route
vitesse_maximale = 5  # Vitesse maximale des véhicules en unités de distance par étape de temps
distance_securite = 2  # Distance de sécurité entre les véhicules

# Dimensions de la fenêtre Pygame
largeur_fenetre = 800
hauteur_fenetre = 200
taille_case = largeur_fenetre // longueur_route

# Initialisation de Pygame
pygame.init()
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
clock = pygame.time.Clock()

# Couleurs
COULEUR_ROUTE = (255, 255, 255)  # Blanc
COULEUR_VEHICULE = (255, 0, 0)  # Rouge

# Création de la grille pour représenter la route
grille = np.zeros((longueur_route, ), dtype=int)

# Initialisation des positions et vitesses des véhicules de manière aléatoire
positions = np.random.choice(np.arange(longueur_route), size=nombre_vehicules, replace=False)
vitesses = np.random.randint(0, vitesse_maximale+1, size=nombre_vehicules)

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer la fenêtre
    fenetre.fill((0, 0, 0))  # Noir

    # Affichage de l'état de la grille
    for i in range(longueur_route):
        x = i * taille_case
        y = hauteur_fenetre // 2

        if i in positions:
            pygame.draw.rect(fenetre, COULEUR_VEHICULE, (x, y, taille_case, taille_case))
        else:
            pygame.draw.rect(fenetre, COULEUR_ROUTE, (x, y, taille_case, taille_case))

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

    # Rafraîchir la fenêtre
    pygame.display.flip()
    clock.tick(10)  # Limiter le taux de rafraîchissement à 10 images par seconde

# Fermer Pygame
pygame.quit()

