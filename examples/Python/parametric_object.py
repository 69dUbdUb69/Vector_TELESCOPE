#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vectorworks Python Example: Parametric Object

Ce script crée un objet paramétrique en demandant les dimensions à l'utilisateur.

Auteur: Vector_TELESCOPE
Date: 2024-08-28
"""

import vs


def create_parametric_rectangle():
    """
    Crée un rectangle avec des dimensions spécifiées par l'utilisateur.
    """
    print("Création d'un rectangle paramétrique...")
    
    # ========================================================================
    # DEMANDER LES PARAMÈTRES À L'UTILISATEUR
    # ========================================================================
    
    # Demander la largeur (valeur par défaut: 100mm)
    width = vs.GetReal("Largeur (mm)", 100.0)
    if width is None:  # Utilisateur a cliqué sur Annuler
        print("Création annulée par l'utilisateur")
        return None
    
    # Demander la hauteur (valeur par défaut: 100mm)
    height = vs.GetReal("Hauteur (mm)", 100.0)
    if height is None:
        print("Création annulée par l'utilisateur")
        return None
    
    # Demander la position X (valeur par défaut: 0mm)
    pos_x = vs.GetReal("Position X (mm)", 0.0)
    if pos_x is None:
        print("Création annulée par l'utilisateur")
        return None
    
    # Demander la position Y (valeur par défaut: 0mm)
    pos_y = vs.GetReal("Position Y (mm)", 0.0)
    if pos_y is None:
        print("Création annulée par l'utilisateur")
        return None
    
    # Demander la couleur
    vs.Message("Choisissez une couleur pour le rectangle:")
    color_choice = vs.GetInteger("1=Rouge, 2=Vert, 3=Bleu, 4=Jaune, 5=Magenta", 1)
    
    # Définir la couleur en fonction du choix
    if color_choice == 1:
        color = vs.RGB(255, 0, 0)  # Rouge
    elif color_choice == 2:
        color = vs.RGB(0, 255, 0)  # Vert
    elif color_choice == 3:
        color = vs.RGB(0, 0, 255)  # Bleu
    elif color_choice == 4:
        color = vs.RGB(255, 255, 0)  # Jaune
    elif color_choice == 5:
        color = vs.RGB(255, 0, 255)  # Magenta
    else:
        color = vs.RGB(200, 200, 200)  # Gris par défaut
    
    # Demander si on veut un remplissage
    fill = vs.GetBoolean("Activer le remplissage?", True)
    
    # ========================================================================
    # CRÉER LE RECTANGLE
    # ========================================================================
    
    # Créer un rectangle centré sur la position spécifiée
    # Rect(x1, y1, x2, y2) où (x1,y1) est le coin inférieur gauche
    # et (x2,y2) est le coin supérieur droit
    rect = vs.Rect(
        pos_x - width/2, pos_y - height/2,
        pos_x + width/2, pos_y + height/2
    )
    
    if rect is None:
        vs.Message("Erreur: Impossible de créer le rectangle!")
        return None
    
    # ========================================================================
    # PERSONNALISER LE RECTANGLE
    # ========================================================================
    
    # Définir la couleur du contour
    vs.SetColor(rect, color)
    
    # Définir l'épaisseur du contour
    vs.SetPenSize(rect, 2)
    
    # Définir le remplissage
    vs.SetFill(rect, fill)
    
    # Définir la couleur de remplissage (plus claire que le contour)
    if fill:
        r, g, b = vs.GetRGB(color)
        fill_color = vs.RGB(
            min(r + 50, 255),  # Augmenter la luminosité
            min(g + 50, 255),
            min(b + 50, 255)
        )
        vs.SetFillColor(rect, fill_color)
    
    # Définir le nom
    vs.SetName(rect, f"Rectangle {width}x{height}")
    
    # Sélectionner le rectangle
    vs.DSelectAll()
    vs.SetSelect(rect)
    
    # Centrer la vue sur le rectangle
    vs.CenterView(rect)
    
    # Mettre à jour l'affichage
    vs.UpdateDisplay()
    
    return rect


def main():
    """Fonction principale."""
    # Créer le rectangle paramétrique
    rect = create_parametric_rectangle()
    
    if rect is not None:
        vs.Message("Rectangle paramétrique créé avec succès!")


# Exécuter le script
if __name__ == "__main__":
    main()
