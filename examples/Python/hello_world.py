#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vectorworks Python Example: Hello World

Ce script affiche simplement un message pour vérifier que Python
fonctionne correctement dans Vectorworks.

Auteur: Vector_TELESCOPE
Date: 2024-08-28
"""

import vs

# Afficher un message dans la console (visible dans l'éditeur de scripts)
print("Hello, Vectorworks from Python!")

# Afficher une boîte de dialogue
vs.Message("Hello, Vectorworks!")

# Afficher un message plus détaillé
vs.Message("""
Bienvenue dans le monde de Python avec Vectorworks!

Ce script démontre que :
- Python est correctement activé
- Le module 'vs' est accessible
- Les boîtes de dialogue fonctionnent

Vous pouvez maintenant explorer les autres exemples!
""")
