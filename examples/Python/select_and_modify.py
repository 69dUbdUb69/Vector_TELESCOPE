#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vectorworks Python Example: Select and Modify

Ce script sélectionne tous les cercles dans le document et les modifie.

Auteur: Vector_TELESCOPE
Date: 2024-08-28
"""

import vs


def modify_selected_objects():
    """Modifie les objets actuellement sélectionnés."""
    # Obtenir les objets sélectionnés
    selected_objects = vs.GetSelectedObjects()
    
    if not selected_objects:
        vs.Message("Aucun objet sélectionné!\nVeuillez sélectionner des objets avant de lancer le script.")
        return 0
    
    count = 0
    
    # Parcourir tous les objets sélectionnés
    for handle in selected_objects:
        # Vérifier si l'objet est un cercle (type 3)
        if vs.GetType(handle) == vs.kObjectTypeCircle:
            # Changer la couleur en rouge
            vs.SetColor(handle, vs.RGB(255, 0, 0))
            
            # Changer le rayon à 100mm
            vs.SetRadius(handle, 100)
            
            # Activer le remplissage
            vs.SetFill(handle, True)
            vs.SetFillColor(handle, vs.RGB(255, 100, 100))
            
            count += 1
    
    # Mettre à jour l'affichage
    vs.UpdateDisplay()
    
    return count


def select_and_modify_circles():
    """Sélectionne tous les cercles et les modifie."""
    # Désélectionner tout
    vs.DSelectAll()
    
    # Obtenir tous les objets de la couche active
    all_objects = vs.FSActLayer()
    
    circles = []
    
    # Parcourir tous les objets pour trouver les cercles
    for handle in all_objects:
        if vs.GetType(handle) == vs.kObjectTypeCircle:
            circles.append(handle)
            vs.SetSelect(handle)  # Sélectionner le cercle
    
    if not circles:
        vs.Message("Aucun cercle trouvé dans le document!")
        return 0
    
    # Modifier les cercles sélectionnés
    count = 0
    for handle in circles:
        # Changer la couleur en rouge
        vs.SetColor(handle, vs.RGB(255, 0, 0))
        
        # Changer le rayon à 100mm
        vs.SetRadius(handle, 100)
        
        # Activer le remplissage
        vs.SetFill(handle, True)
        vs.SetFillColor(handle, vs.RGB(255, 100, 100))
        
        count += 1
    
    # Mettre à jour l'affichage
    vs.UpdateDisplay()
    
    return count


def main():
    """Fonction principale."""
    print("Exécution du script Select and Modify...")
    
    # Demander à l'utilisateur quelle action effectuer
    vs.Message("Ce script peut :\n1. Modifier les objets actuellement sélectionnés\n2. Sélectionner et modifier tous les cercles")
    
    choice = vs.GetInteger("Choix (1 ou 2)", 1)
    
    if choice == 1:
        # Modifier les objets sélectionnés
        count = modify_selected_objects()
        vs.Message(f"{count} objets sélectionnés modifiés!")
    elif choice == 2:
        # Sélectionner et modifier tous les cercles
        count = select_and_modify_circles()
        vs.Message(f"{count} cercles trouvés et modifiés!")
    else:
        vs.Message("Choix invalide!")


# Exécuter le script
if __name__ == "__main__":
    main()
