import numpy as np
import matplotlib.pyplot as plt

# Paramètres du modèle
longueur_route = 50  # Longueur de la route en unités
nombre_vehicules = 20  # Nombre de véhicules sur la route
vitesse_maximale = 5  # Vitesse maximale des véhicules en unités de distance par étape de temps
distance_securite = 2  # Distance de sécurité entre les véhicules

# Constante pour les données d'entrée
constante_ajoutee = 2

# Création de la grille pour représenter la route
grille = np.zeros((longueur_route, ), dtype=int)

# Initialisation des positions et vitesses des véhicules de manière aléatoire
positions = np.random.choice(np.arange(longueur_route), size=nombre_vehicules, replace=False)
vitesses = np.random.randint(0, vitesse_maximale+1, size=nombre_vehicules)

# Listes pour stocker les données collectées
densite_trafic = []
vitesses_moyennes = []
temps_trajet = []

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

    # Collecte des données pertinentes à chaque étape de temps
    densite_trafic.append(len(positions) / longueur_route)
    vitesses_moyennes.append(np.mean(vitesses))
    temps_trajet.append(np.sum(longueur_route - np.array(positions)))

# Calcul de la densité du trafic
densite_trafic = np.array(densite_trafic)

# Calcul de l'évolution de la vitesse moyenne
vitesses_moyennes = np.array(vitesses_moyennes)

# Calcul de la moyenne des temps de trajet
temps_trajet = np.array(temps_trajet)
moyenne_temps_trajet = np.mean(temps_trajet)

# Évaluation de la congestion du trafic
congestion_trafic = vitesses_moyennes < vitesse_maximale

# Visualisation des résultats
temps = np.arange(1, 11)

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(temps, densite_trafic)
plt.title("Évolution de la densité du trafic")
plt.xlabel("Temps")
plt.ylabel("Densité du trafic")

plt.subplot(3, 1, 2)
plt.plot(temps, vitesses_moyennes)
plt.title("Évolution de la vitesse moyenne")
plt.xlabel("Temps")
plt.ylabel("Vitesse moyenne")

plt.subplot(3, 1, 3)
plt.bar(temps, temps_trajet)
plt.axhline(moyenne_temps_trajet, color='r', linestyle='--', label="Moyenne")
plt.title("Temps de trajet")
plt.xlabel("Temps")
plt.ylabel("Temps de trajet")
plt.legend()

plt.tight_layout()
plt.show()
