import numpy as np

# Paramètres du modèle
nombre_conducteurs = 2
strategies_initiales = np.array([[0, 1], [1, 0]])  # Stratégies initiales des conducteurs
gains = np.array([[2, 4], [4, 2]])  # Matrice des gains

# Fonction pour calculer les gains des conducteurs
def calculer_gains(strategies):
    gains_conducteurs = np.zeros(nombre_conducteurs)
    for i in range(nombre_conducteurs):
        gains_conducteurs[i] = gains[i][np.sum(strategies, axis=0)[i]]
    return gains_conducteurs

# Boucle d'itération pour trouver l'équilibre de Nash
iterations = 10
strategies = strategies_initiales.copy()

for it in range(iterations):
    print(f"Itération {it + 1}:")
    print("Stratégies des conducteurs:", strategies)
    print("Gains des conducteurs:", calculer_gains(strategies))

    nouvelles_strategies = strategies.copy()

    for i in range(nombre_conducteurs):
        autre_conducteur = 1 - i
        meilleure_strategie = np.argmax(calculer_gains(strategies[:, autre_conducteur]))
        nouvelles_strategies[i] = np.zeros(strategies.shape[1])
        nouvelles_strategies[i, meilleure_strategie] = 1

    if np.array_equal(strategies, nouvelles_strategies):
        break

    strategies = nouvelles_strategies

print("\nStratégies d'équilibre de Nash atteintes:")
print("Stratégies des conducteurs:", strategies)
print("Gains des conducteurs:", calculer_gains(strategies))

