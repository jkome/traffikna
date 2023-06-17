import time
import random

# Densité du trafic sur chaque voie (valeurs arbitraires pour l'exemple)
densite_voie1 = 0.8
densite_voie2 = 0.5

# Durée initiale des feux de signalisation
duree_feu_vert_voie1 = 30
duree_feu_vert_voie2 = 20

while True:
    # Affichage de l'état des feux de signalisation
    print("Voie 1 :", "Vert" if duree_feu_vert_voie1 > 0 else "Rouge")
    print("Voie 2 :", "Vert" if duree_feu_vert_voie2 > 0 else "Rouge")

    # Simulation du trafic pendant la durée des feux de signalisation
    time.sleep(1)  # Attente d'une seconde

    # Mise à jour de la densité du trafic (simulation aléatoire pour l'exemple)
    densite_voie1 += random.uniform(-0.1, 0.1)
    densite_voie2 += random.uniform(-0.1, 0.1)

    # Ajustement de la durée des feux de signalisation en fonction de la densité
    duree_feu_vert_voie1 -= densite_voie1 * 2
    duree_feu_vert_voie2 -= densite_voie2 * 2

    # Vérification et correction des durées négatives
    if duree_feu_vert_voie1 < 0:
        duree_feu_vert_voie1 = 0
    if duree_feu_vert_voie2 < 0:
        duree_feu_vert_voie2 = 0

    # Inversion des feux de signalisation lorsque la durée atteint 0
    if duree_feu_vert_voie1 == 0 and duree_feu_vert_voie2 == 0:
        duree_feu_vert_voie1 = 30
        duree_feu_vert_voie2 = 20

    print()  # Ligne vide pour la clarté de l'affichage
