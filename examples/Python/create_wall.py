#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vectorworks Python Example: Create Wall

Ce script crée un mur avec des paramètres personnalisables.

Auteur: Vector_TELESCOPE
Date: 2024-08-28
"""

import vs


def create_custom_wall(x, y, length, height, thickness, material_name=None, color=None):
    """
    Crée un mur personnalisé avec les paramètres spécifiés.
    
    Args:
        x (float): Position X de départ (en mm)
        y (float): Position Y de départ (en mm)
        length (float): Longueur du mur (en mm)
        height (float): Hauteur du mur (en mm)
        thickness (float): Épaisseur du mur (en mm)
        material_name (str, optional): Nom du matériau. Si None, utilise le matériau par défaut.
        color (tuple, optional): Couleur RGB (r, g, b). Si None, utilise la couleur par défaut.
    
    Returns:
        handle: Référence au mur créé
    """
    # Créer le mur
    wall = vs.Wall(x, y, length, height, thickness)
    
    if wall is None:
        vs.Message("Erreur: Impossible de créer le mur!")
        return None
    
    # Définir le matériau si spécifié
    if material_name is not None:
        try:
            vs.SetWallMaterial(wall, material_name)
        except Exception as e:
            print(f"Avertissement: Impossible de définir le matériau '{material_name}': {e}")
    
    # Définir la couleur si spécifiée
    if color is not None:
        vs.SetColor(wall, vs.RGB(*color))
    
    # Définir le nom
    vs.SetName(wall, f"Mur {length/1000}m x {height/1000}m")
    
    return wall


def main():
    """Fonction principale."""
    print("Création d'un mur personnalisé...")
    
    # ========================================================================
    # PARAMÈTRES DU MUR
    # ========================================================================
    
    # Position de départ (en mm)
    start_x = 0
    start_y = 0
    
    # Dimensions du mur (en mm)
    wall_length = 5000    # 5 mètres
    wall_height = 3000    # 3 mètres
    wall_thickness = 200  # 20 cm
    
    # Couleur (R, V, B) - Marron pour un mur en brique
    wall_color = (200, 100, 50)
    
    # Nom du matériau (doit exister dans votre bibliothèque)
    # Essayez différents noms comme 'Brique', 'Béton', 'Bois', etc.
    material_name = 'Brique'
    
    # ========================================================================
    # CRÉATION DU MUR
    # ========================================================================
    
    # Créer le mur
    wall = create_custom_wall(
        x=start_x,
        y=start_y,
        length=wall_length,
        height=wall_height,
        thickness=wall_thickness,
        material_name=material_name,
        color=wall_color
    )
    
    if wall is None:
        return
    
    # Sélectionner le mur
    vs.DSelectAll()
    vs.SetSelect(wall)
    
    # Centrer la vue sur le mur
    vs.CenterView(wall)
    
    # Mettre à jour l'affichage
    vs.UpdateDisplay()
    
    # Afficher un message de confirmation
    vs.Message(f"""
Mur créé avec succès!

Paramètres :
- Position: ({start_x/1000}m, {start_y/1000}m)
- Longueur: {wall_length/1000}m
- Hauteur: {wall_height/1000}m
- Épaisseur: {wall_thickness/10}cm
- Matériau: {material_name}

Conseils :
- Essayez de modifier les paramètres dans le code
- Testez avec différents matériaux
- Créez plusieurs murs avec des paramètres différents
""")


# Exécuter le script
if __name__ == "__main__":
    main()
