#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vectorworks Python Example: Draw Shapes

Ce script dessine différentes formes géométriques pour démontrer
les fonctions de création d'objets de base.

Auteur: Vector_TELESCOPE
Date: 2024-08-28
"""

import vs


def main():
    """Fonction principale qui dessine les formes."""
    
    # Désélectionner tout avant de commencer
    vs.DSelectAll()
    
    print("Création des formes géométriques...")
    
    # ========================================================================
    # DESSINER UNE LIGNE
    # ========================================================================
    print("Création d'une ligne...")
    line = vs.Line(0, 0, 100, 100)
    vs.SetColor(line, vs.RGB(255, 0, 0))  # Rouge
    vs.SetPenSize(line, 2)  # Épaisseur de 2mm
    vs.SetName(line, "Ligne Rouge")
    
    # ========================================================================
    # DESSINER UN CERCLE
    # ========================================================================
    print("Création d'un cercle...")
    circle = vs.Circle(200, 0, 50)  # Centre (200,0), rayon 50mm
    vs.SetColor(circle, vs.RGB(0, 0, 255))  # Bleu
    vs.SetPenSize(circle, 2)
    vs.SetFill(circle, True)  # Activer le remplissage
    vs.SetFillColor(circle, vs.RGB(100, 100, 255))  # Bleu clair pour le remplissage
    vs.SetName(circle, "Cercle Bleu")
    
    # ========================================================================
    # DESSINER UN RECTANGLE
    # ========================================================================
    print("Création d'un rectangle...")
    # Rect(x1, y1, x2, y2) - coin inférieur gauche et coin supérieur droit
    rect = vs.Rect(0, -100, 100, -50)
    vs.SetColor(rect, vs.RGB(0, 255, 0))  # Vert
    vs.SetPenSize(rect, 2)
    vs.SetFill(rect, True)
    vs.SetFillColor(rect, vs.RGB(0, 200, 0))  # Vert clair
    vs.SetName(rect, "Rectangle Vert")
    
    # ========================================================================
    # DESSINER UN POLYGONE
    # ========================================================================
    print("Création d'un polygone...")
    # Polygon(num_sides, x, y, radius) - nombre de côtés, centre, rayon
    polygon = vs.Polygon(5, 200, -100, 50)  # Pentagone
    vs.SetColor(polygon, vs.RGB(255, 255, 0))  # Jaune
    vs.SetPenSize(polygon, 2)
    vs.SetFill(polygon, True)
    vs.SetFillColor(polygon, vs.RGB(255, 255, 100))  # Jaune clair
    vs.SetName(polygon, "Pentagone Jaune")
    
    # ========================================================================
    # DESSINER UNE ÉTOILE
    # ========================================================================
    print("Création d'une étoile...")
    # Star(num_points, outer_radius, inner_radius, x, y)
    star = vs.Star(5, 50, 25, 400, -100)  # Étoile à 5 branches
    vs.SetColor(star, vs.RGB(255, 100, 255))  # Magenta
    vs.SetPenSize(star, 2)
    vs.SetFill(star, True)
    vs.SetFillColor(star, vs.RGB(255, 150, 255))  # Magenta clair
    vs.SetName(star, "Étoile Magenta")
    
    # ========================================================================
    # DESSINER DU TEXTE
    # ========================================================================
    print("Création de texte...")
    text = vs.Text(200, -200, "Formes créées avec Python!")
    vs.SetTextSize(text, 12)  # Taille de la police
    vs.SetTextColor(text, vs.RGB(0, 0, 0))  # Noir
    vs.SetName(text, "Texte Python")
    
    # ========================================================================
    # SÉLECTIONNER TOUS LES OBJETS CRÉÉS
    # ========================================================================
    vs.SetSelect(line)
    vs.SetSelect(circle)
    vs.SetSelect(rect)
    vs.SetSelect(polygon)
    vs.SetSelect(star)
    vs.SetSelect(text)
    
    # Mettre à jour l'affichage
    vs.UpdateDisplay()
    
    # Afficher un message de confirmation
    vs.Message("Toutes les formes ont été créées avec succès!\n\n" +
               "Vous pouvez maintenant :\n" +
               "- Modifier les propriétés des objets\n" +
               "- Déplacer les objets\n" +
               "- Supprimer les objets\n" +
               "- Explorer le code pour comprendre comment ça marche!")


# Exécuter le script
if __name__ == "__main__":
    main()
