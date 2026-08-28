#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vectorworks Python Example: Batch Rename

Ce script renomme plusieurs objets sélectionnés avec un préfixe et un numéro.

Auteur: Vector_TELESCOPE
Date: 2024-08-28
"""

import vs


def batch_rename():
    """
    Renomme les objets sélectionnés avec un préfixe et un numéro séquentiel.
    """
    print("Exécution du renommage par lots...")
    
    # ========================================================================
    # DEMANDER LE PRÉFIXE
    # ========================================================================
    
    # Demander le préfixe à l'utilisateur
    prefix = vs.GetString("Préfixe pour le renommage", "Objet")
    if prefix is None:  # Utilisateur a cliqué sur Annuler
        print("Renommage annulé par l'utilisateur")
        return 0
    
    # ========================================================================
    # VÉRIFIER LA SÉLECTION
    # ========================================================================
    
    # Obtenir les objets sélectionnés
    selected_objects = vs.GetSelectedObjects()
    
    if not selected_objects:
        vs.Message("Aucun objet sélectionné!\nVeuillez sélectionner des objets avant de lancer le script.")
        return 0
    
    num_objects = len(selected_objects)
    
    # ========================================================================
    # RENAME LES OBJETS
    # ========================================================================
    
    # Initialiser le compteur
    count = 1
    renamed_count = 0
    
    # Parcourir tous les objets sélectionnés
    for handle in selected_objects:
        # Créer un nouveau nom avec le préfixe et un numéro
        new_name = f"{prefix} {count}"
        
        # Renommer l'objet
        vs.SetName(handle, new_name)
        
        # Incrémenter le compteur
        count += 1
        renamed_count += 1
    
    # ========================================================================
    # AFFICHER UN RAPPORT
    # ========================================================================
    
    # Afficher un message de confirmation
    vs.Message(f"""
Renommage terminé avec succès!

- Nombre d'objets renommés: {renamed_count}
- Préfixe utilisé: "{prefix}"
- Format: "{prefix} 1", "{prefix} 2", etc.

Les objets ont été renommés dans l'ordre de la sélection.
""")
    
    return renamed_count


def advanced_batch_rename():
    """
    Renommage avancé avec plus d'options.
    """
    print("Renommage avancé...")
    
    # Demander le préfixe
    prefix = vs.GetString("Préfixe", "Objet")
    if prefix is None:
        return 0
    
    # Demander le suffixe
    suffix = vs.GetString("Suffixe (laisser vide si aucun)", "")
    if suffix is None:
        return 0
    
    # Demander le numéro de départ
    start_num = vs.GetInteger("Numéro de départ", 1)
    if start_num is None:
        return 0
    
    # Demander l'incrément
    increment = vs.GetInteger("Incrément", 1)
    if increment is None or increment <= 0:
        increment = 1
    
    # Obtenir les objets sélectionnés
    selected_objects = vs.GetSelectedObjects()
    
    if not selected_objects:
        vs.Message("Aucun objet sélectionné!")
        return 0
    
    # Renommer les objets
    current_num = start_num
    renamed_count = 0
    
    for handle in selected_objects:
        new_name = f"{prefix}{current_num}{suffix}"
        vs.SetName(handle, new_name)
        current_num += increment
        renamed_count += 1
    
    vs.Message(f"{renamed_count} objets renommés avec le format: {prefix}{start_num}{suffix}, {prefix}{start_num + increment}{suffix}, ...")
    return renamed_count


def main():
    """Fonction principale."""
    vs.Message("""
Script de renommage par lots

Ce script permet de renommer plusieurs objets en une seule fois.

Options :
1. Renommage simple (préfixe + numéro)
2. Renommage avancé (préfixe + numéro + suffixe + incrément)
""")
    
    choice = vs.GetInteger("Choix (1 ou 2)", 1)
    
    if choice == 1:
        count = batch_rename()
    elif choice == 2:
        count = advanced_batch_rename()
    else:
        vs.Message("Choix invalide!")
        return
    
    if count > 0:
        print(f"{count} objets ont été renommés")


# Exécuter le script
if __name__ == "__main__":
    main()
