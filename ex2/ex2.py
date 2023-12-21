
import math

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculer_distance_totale(pizzerias, commandes):
    distance_totale = 0

    for commande in commandes:
        distance_min = math.inf

        for pizzeria in pizzerias:
            d = distance(pizzeria[0], pizzeria[1], commande[0], commande[1])
            distance_min = min(distance_min, d)

        distance_totale += distance_min * 2  # Aller-retour

    return distance_totale

N, M = map(int, input().split())

pizzerias = [tuple(map(int, input().split())) for _ in range(N)]
commandes = [tuple(map(int, input().split())) for _ in range(M)]

# Calcul de la distance totale
resultat = calculer_distance_totale(pizzerias, commandes)

# Affichage du résultat
print(resultat)
