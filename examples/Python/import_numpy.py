#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vectorworks Python Example: Import NumPy

Ce script démontre comment utiliser des bibliothèques Python externes
comme NumPy pour des calculs mathématiques avancés.

Auteur: Vector_TELESCOPE
Date: 2024-08-28
"""

import vs


def main():
    """Fonction principale."""
    print("Test de l'importation de NumPy...")
    
    # ========================================================================
    # ESSAYER D'IMPORTER NUMPY
    # ========================================================================
    
    try:
        import numpy as np
        print("NumPy importé avec succès!")
        
        # ========================================================================
        # EXEMPLE 1: CRÉER DES POINTS AVEC NUMPY
        # ========================================================================
        
        print("\nExemple 1: Création de points avec NumPy")
        
        # Créer un tableau de points avec NumPy
        # Chaque ligne représente un point (x, y)
        points_array = np.array([
            [0, 0],
            [100, 50],
            [200, 0],
            [300, 100],
            [400, 0]
        ])
        
        print(f"Points générés:\n{points_array}")
        
        # Dessiner des lignes entre les points
        vs.DSelectAll()
        
        for i in range(len(points_array) - 1):
            x1, y1 = points_array[i]
            x2, y2 = points_array[i + 1]
            line = vs.Line(x1, y1, x2, y2)
            vs.SetColor(line, vs.RGB(255, 0, 0))  # Rouge
            vs.SetPenSize(line, 2)
        
        # ========================================================================
        # EXEMPLE 2: CALCULS MATHÉMATIQUES AVEC NUMPY
        # ========================================================================
        
        print("\nExemple 2: Calculs mathématiques avec NumPy")
        
        # Créer un cercle avec des points calculés avec NumPy
        num_points = 20
        radius = 100
        center_x, center_y = 200, -200
        
        # Calculer les angles (en radians)
        angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
        
        # Calculer les coordonnées des points
        x_coords = center_x + radius * np.cos(angles)
        y_coords = center_y + radius * np.sin(angles)
        
        print(f"Angles: {angles}")
        print(f"Coordonnées X: {x_coords}")
        print(f"Coordonnées Y: {y_coords}")
        
        # Dessiner le cercle point par point
        for i in range(len(x_coords) - 1):
            x1, y1 = x_coords[i], y_coords[i]
            x2, y2 = x_coords[i + 1], y_coords[i + 1]
            line = vs.Line(x1, y1, x2, y2)
            vs.SetColor(line, vs.RGB(0, 0, 255))  # Bleu
            vs.SetPenSize(line, 2)
        
        # Fermer le cercle
        line = vs.Line(x_coords[-1], y_coords[-1], x_coords[0], y_coords[0])
        vs.SetColor(line, vs.RGB(0, 0, 255))
        vs.SetPenSize(line, 2)
        
        # ========================================================================
        # EXEMPLE 3: OPÉRATIONS MATRICIELLES
        # ========================================================================
        
        print("\nExemple 3: Opérations matricielles")
        
        # Créer une matrice de transformation
        # Translation de 100mm en X et 50mm en Y
        translation_matrix = np.array([[1, 0, 100],
                                        [0, 1, 50],
                                        [0, 0, 1]])
        
        # Appliquer la translation à nos points
        # Ajouter une colonne de 1 pour les coordonnées homogènes
        homogeneous_points = np.column_stack((points_array, np.ones(len(points_array))))
        translated_points = np.dot(homogeneous_points, translation_matrix.T)
        
        print(f"Points traduits:\n{translated_points}")
        
        # Dessiner les lignes traduites
        for i in range(len(translated_points) - 1):
            x1, y1, _ = translated_points[i]
            x2, y2, _ = translated_points[i + 1]
            line = vs.Line(x1, y1, x2, y2)
            vs.SetColor(line, vs.RGB(0, 255, 0))  # Vert
            vs.SetPenSize(line, 2)
        
        # ========================================================================
        # EXEMPLE 4: STATISTIQUES
        # ========================================================================
        
        print("\nExemple 4: Statistiques avec NumPy")
        
        # Calculer des statistiques sur nos points
        all_x = points_array[:, 0]
        all_y = points_array[:, 1]
        
        print(f"Moyenne X: {np.mean(all_x)}")
        print(f"Moyenne Y: {np.mean(all_y)}")
        print(f"Écart-type X: {np.std(all_x)}")
        print(f"Écart-type Y: {np.std(all_y)}")
        print(f"Distance totale: {np.sum(np.sqrt(np.diff(x_coords)**2 + np.diff(y_coords)**2))}")
        
        # ========================================================================
        # AFFICHER UN MESSAGE DE RÉUSSITE
        # ========================================================================
        
        vs.Message("""
NumPy fonctionne avec Vectorworks!

Ce script a démontré :
- L'importation de bibliothèques externes
- La création de tableaux NumPy
- Les calculs mathématiques avancés
- Les opérations matricielles
- Les statistiques

Note: Toutes les bibliothèques Python standard
ne sont pas disponibles dans Vectorworks.
Seules les bibliothèques incluses avec la version
Python de Vectorworks sont accessibles.
""")
        
    except ImportError as e:
        print(f"NumPy n'est pas disponible: {e}")
        vs.Message("""
NumPy n'est pas disponible dans cet environnement.

Cela peut être dû à :
1. NumPy n'est pas installé avec la version Python de Vectorworks
2. L'environnement Python est restreint

Essayez avec d'autres bibliothèques standard comme 'math' ou 'random'
qui sont généralement disponibles.
""")
        
        # Montrer un exemple avec le module math standard
        import math
        print("\nUtilisation du module math standard...")
        
        vs.DSelectAll()
        
        # Dessiner un cercle avec le module math
        center_x, center_y = 100, -100
        radius = 50
        num_points = 36
        
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x1 = center_x + radius * math.cos(angle)
            y1 = center_y + radius * math.sin(angle)
            angle2 = 2 * math.pi * (i + 1) / num_points
            x2 = center_x + radius * math.cos(angle2)
            y2 = center_y + radius * math.sin(angle2)
            
            line = vs.Line(x1, y1, x2, y2)
            vs.SetColor(line, vs.RGB(255, 100, 0))  # Orange
            vs.SetPenSize(line, 2)
        
        vs.Message("Cercle créé avec le module math standard!")


# Exécuter le script
if __name__ == "__main__":
    main()
