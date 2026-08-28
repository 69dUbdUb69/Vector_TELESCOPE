# 🐍 Python Example

Ce dossier contient des exemples de scripts **Python** pour Vectorworks. Depuis Vectorworks 2021, il est possible d'écrire des scripts en Python pour automatiser des tâches, créer des objets et étendre les fonctionnalités du logiciel.

---

## 📚 Ce que vous allez apprendre

✅ Syntaxe de base de Python
✅ Utilisation du module `vs` (Vectorworks Scripting)
✅ Création et manipulation d'objets Vectorworks
✅ Automatisation de tâches avec Python
✅ Avantages de Python par rapport à VectorScript

---

## 🎯 Avantages et Inconvénients

### ✅ Avantages de Python

- **Syntaxe moderne et lisible** : Plus facile à apprendre et à maintenir
- **Typage dynamique** : Pas besoin de déclarer les types de variables
- **Bibliothèques riches** : Accès à de nombreuses bibliothèques standard
- **Gestion de la mémoire automatique** : Pas de fuites mémoire avec le garbage collection
- **Indentation obligatoire** : Code plus lisible et structuré
- **Communauté active** : Beaucoup de ressources et de support disponibles
- **Multiplateforme** : Fonctionne sur Windows et macOS

### ❌ Inconvénients de Python

- **Performances** : Plus lent que le C++ pour les opérations intensives
- **Accès limité à l'API** : Certaines fonctionnalités ne sont pas disponibles
- **Pas de compilation** : Les erreurs ne sont détectées qu'à l'exécution
- **Environnement isolé** : Accès limité aux bibliothèques externes
- **Moins mature** : Moins documenté que VectorScript pour Vectorworks

---

## 🛠️ Prérequis

- ✅ Vectorworks 2021+ installé
- ✅ Python activé dans les préférences de Vectorworks

---

## 🚀 Utilisation de Python dans Vectorworks

### 1️⃣ Activer Python

1. Allez dans **Outils > Préférences > VectorScript/Python**
2. Cochez **Enable Python Scripting**
3. Cliquez sur **OK**
4. Redémarrez Vectorworks si nécessaire

### 2️⃣ Ouvrir l'éditeur de scripts

1. Dans Vectorworks, allez dans **Outils > Scripts > Éditeur de Scripts**
2. Ou utilisez le raccourci **Ctrl+Shift+S** (Windows) / **Cmd+Shift+S** (macOS)

### 3️⃣ Créer un nouveau script Python

1. Cliquez sur **Nouveau** dans l'éditeur de scripts
2. Sélectionnez **Python** comme langage
3. Donnez un nom à votre script
4. Commencez à coder !

### 4️⃣ Exécuter un script

- Cliquez sur **Exécuter** (▶️) ou appuyez sur **F5**
- Ou cliquez sur **Exécuter le Script** dans le menu

### 5️⃣ Enregistrer un script

- Cliquez sur **Enregistrer** pour sauvegarder votre script
- Les scripts Python sont sauvegardés avec l'extension `.py`

---

## 📁 Exemples fournis

### 1. [hello_world.py](hello_world.py)

Le script le plus simple : affiche un message dans la console.

**Code :**
```python
import vs

# Afficher un message dans la console
print("Hello, Vectorworks from Python!")

# Afficher une boîte de dialogue
vs.Message("Hello, Vectorworks!")
```

---

### 2. [draw_shapes.py](draw_shapes.py)

Dessine différentes formes géométriques.

**Fonctionnalités :**
- Dessine une ligne rouge
- Dessine un cercle bleu
- Dessine un rectangle vert
- Dessine un polygone jaune

**Code :**
```python
import vs

# Désélectionner tout
vs.DSelectAll()

# Dessiner une ligne
line = vs.Line(0, 0, 100, 100)
vs.SetColor(line, vs.RGB(255, 0, 0))  # Rouge
vs.SetPenSize(line, 2)

# Dessiner un cercle
circle = vs.Circle(200, 0, 50)
vs.SetColor(circle, vs.RGB(0, 0, 255))  # Bleu
vs.SetPenSize(circle, 2)
vs.SetFill(circle, True)
vs.SetFillColor(circle, vs.RGB(100, 100, 255))

# ... etc
```

---

### 3. [create_wall.py](create_wall.py)

Crée un mur avec des paramètres personnalisables.

**Fonctionnalités :**
- Crée un mur rectiligne
- Définit la hauteur, l'épaisseur et le matériau
- Positionne le mur à une position spécifique

---

### 4. [select_and_modify.py](select_and_modify.py)

Sélectionne tous les objets d'un certain type et les modifie.

**Fonctionnalités :**
- Sélectionne tous les cercles dans le document
- Change leur couleur en rouge
- Change leur rayon

---

### 5. [parametric_object.py](parametric_object.py)

Crée un objet paramétrique avec une interface utilisateur.

**Fonctionnalités :**
- Utilise `vs.GetReal()` pour demander des valeurs à l'utilisateur
- Crée un rectangle avec les dimensions spécifiées
- Montre comment utiliser les boîtes de dialogue

---

### 6. [batch_rename.py](batch_rename.py)

Renomme plusieurs objets en une seule fois.

**Fonctionnalités :**
- Demande un préfixe à l'utilisateur
- Renomme tous les objets sélectionnés avec ce préfixe
- Ajoute un numéro séquentiel

---

### 7. [import_numpy.py](import_numpy.py)

Montre comment utiliser des bibliothèques Python externes comme NumPy.

**Fonctionnalités :**
- Utilise NumPy pour des calculs mathématiques
- Crée des points basés sur des calculs NumPy
- Dessine des lignes entre ces points

---

## 🐍 Syntaxe de base de Python

### Variables et types

```python
# Déclaration de variables (pas de type nécessaire)
x = 10          # Entier
y = 10.5        # Nombre décimal
name = "Hello"  # Chaîne de caractères
active = True  # Booléen

# Listes (tableaux dynamiques)
points = [ (0, 0), (10, 10), (20, 0) ]

# Dictionnaires (tableaux associatifs)
params = {
    "width": 100,
    "height": 50,
    "color": "red"
}
```

---

### Structures de contrôle

#### Condition IF

```python
if x > 10:
    print("x est supérieur à 10")
elif x == 10:
    print("x vaut 10")
else:
    print("x est inférieur à 10")
```

#### Boucle FOR

```python
# Parcourir une liste
for point in points:
    print(f"Point: {point}")

# Boucle avec range
for i in range(5):  # 0 à 4
    print(f"i = {i}")

# Boucle avec index
for i, point in enumerate(points):
    print(f"Index {i}: {point}")
```

#### Boucle WHILE

```python
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1
```

---

### Fonctions

```python
# Définition d'une fonction
def calculate_area(width, height):
    """Calcule l'aire d'un rectangle."""
    return width * height

# Appel de la fonction
area = calculate_area(10, 20)
print(f"Area: {area}")

# Fonction avec valeur par défaut
def greet(name="World"):
    print(f"Hello, {name}!")

greet()  # Affiche "Hello, World!"
greet("Alice")  # Affiche "Hello, Alice!"
```

---

### Classes et objets

```python
# Définition d'une classe
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Création d'une instance
rect = Rectangle(10, 20)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
```

---

## 🔧 Le module `vs` (Vectorworks Scripting)

Le module `vs` est le module principal pour interagir avec Vectorworks depuis Python.

### Importation

```python
import vs
```

### Constantes utiles

```python
# Couleurs
vs.RGB(255, 0, 0)       # Rouge
vs.RGB(0, 255, 0)       # Vert
vs.RGB(0, 0, 255)       # Bleu

# Types d'objets
vs.kObjectTypeLine      # Ligne
vs.kObjectTypeCircle    # Cercle
vs.kObjectTypeRect      # Rectangle
vs.kObjectTypePolygon   # Polygone
```

---

### Fonctions de création d'objets

```python
# Créer une ligne
line = vs.Line(x1, y1, x2, y2)

# Créer un cercle
circle = vs.Circle(x, y, radius)

# Créer un rectangle
rect = vs.Rect(x1, y1, x2, y2)

# Créer un polygone régulier
polygon = vs.Polygon(num_sides, x, y, radius)

# Créer du texte
text = vs.Text(x, y, "Mon texte")

# Créer un mur
wall = vs.Wall(x, y, length, height, thickness)
```

---

### Manipulation d'objets

```python
# Sélectionner/désélectionner
vs.SetSelect(handle)      # Sélectionner un objet
vs.DSelect(handle)        # Désélectionner un objet
vs.DSelectAll()           # Désélectionner tout

# Définir la couleur
vs.SetColor(handle, vs.RGB(r, g, b))  # Couleur du contour
vs.SetPenColor(handle, vs.RGB(r, g, b))
vs.SetFillColor(handle, vs.RGB(r, g, b))  # Couleur de remplissage

# Définir l'épaisseur du contour
vs.SetPenSize(handle, size)

# Définir le remplissage
vs.SetFill(handle, True)  # Activer le remplissage
vs.SetFill(handle, False) # Désactiver le remplissage

# Déplacer un objet
vs.Move(handle, dx, dy)

# Tourner un objet
vs.Rotate(handle, angle_in_degrees)

# Redimensionner un objet
vs.Scale(handle, scale_factor)

# Supprimer un objet
vs.Delete(handle)

# Définir le nom
vs.SetName(handle, "Mon Objet")

# Obtenir le type
object_type = vs.GetType(handle)
```

---

### Accès aux propriétés

```python
# Position
x, y = vs.GetObjectPosition(handle)

# Taille
width = vs.GetWidth(handle)
height = vs.GetHeight(handle)

# Rayon (pour les cercles)
radius = vs.GetRadius(handle)

# Nom
name = vs.GetName(handle)

# Sélection
is_selected = vs.GetSelect(handle)
```

---

### Itération sur les objets

```python
# Parcourir tous les objets de la couche active
for handle in vs.FSActLayer():
    print(f"Objet: {handle}, Type: {vs.GetType(handle)}")

# Parcourir les objets sélectionnés
for handle in vs.GetSelectedObjects():
    vs.SetColor(handle, vs.RGB(255, 0, 0))  # Colorier en rouge

# Itérateur avancé
iter = vs.VWObjectIterator(vs.kVWSelectionSetActive)
handle = iter.Next()
while handle:
    # Traiter l'objet
    handle = iter.Next()
```

---

### Boîtes de dialogue

```python
# Afficher un message
vs.Message("Mon message")

# Demander une confirmation
result = vs.Alert("Voulez-vous continuer?", vs.kVWAlertOKCancel, vs.kVWAlertQuestion)
if result == vs.kVWAlertOK:
    print("Utilisateur a cliqué sur OK")

# Demander un nombre
width = vs.GetReal("Largeur (mm)", 100.0)

# Demander un entier
count = vs.GetInteger("Nombre", 1)

# Demander une chaîne
name = vs.GetString("Nom", "Mon Objet")

# Demander un booléen
active = vs.GetBoolean("Activer?", True)
```

---

### Couleurs

```python
# Créer une couleur RGB
red = vs.RGB(255, 0, 0)
green = vs.RGB(0, 255, 0)
blue = vs.RGB(0, 0, 255)

# Créer une couleur avec alpha (transparence)
transparent_red = vs.RGBA(255, 0, 0, 128)

# Obtenir les composantes d'une couleur
r, g, b = vs.GetRGB(red)
```

---

### Points et géométrie

```python
# Créer un point 2D
pt1 = vs.VWPoint2D(10, 20)
pt2 = vs.VWPoint2D(50, 100)

# Créer un point 3D
pt3d = vs.VWPoint3D(10, 20, 30)

# Calculer la distance entre deux points
distance = vs.Distance(pt1, pt2)

# Créer un vecteur
vector = vs.VWVector2D(10, 20)
```

---

## 🎨 Bonnes pratiques

### 1. Commenter votre code

```python
# Commentaire sur une ligne

"""
Commentaire sur plusieurs lignes
(Docstring pour les fonctions et classes)
"""

def ma_fonction(param):
    """
    Description de la fonction.
    
    Args:
        param: Description du paramètre
    
    Returns:
        Description de la valeur de retour
    """
    pass
```

### 2. Gérer les erreurs

```python
try:
    # Code qui peut échouer
    handle = vs.Line(0, 0, 10, 10)
    if handle is None:
        raise ValueError("Impossible de créer la ligne")
    
except ValueError as e:
    print(f"Erreur: {e}")
except Exception as e:
    print(f"Erreur inattendue: {e}")
finally:
    # Code exécuté dans tous les cas
    print("Nettoyage...")
```

### 3. Utiliser des constantes

```python
# Constantes en majuscules
DEFAULT_WIDTH = 100.0
DEFAULT_HEIGHT = 50.0
DEFAULT_COLOR = vs.RGB(255, 0, 0)

# Utilisation
rect = vs.Rect(0, 0, DEFAULT_WIDTH, DEFAULT_HEIGHT)
vs.SetColor(rect, DEFAULT_COLOR)
```

### 4. Structurer votre code

```python
"""
Mon Script Vectorworks
Description: Ce script fait ceci et cela
Auteur: Moi
Date: 2024-08-28
"""

import vs

# Constantes
DEFAULT_SIZE = 100.0

# Fonctions utilitaires
def create_rectangle(x, y, width, height):
    """Crée un rectangle à la position spécifiée."""
    rect = vs.Rect(x, y, x + width, y + height)
    vs.SetFill(rect, True)
    vs.SetFillColor(rect, vs.RGB(200, 200, 255))
    return rect

# Fonction principale
def main():
    """Fonction principale du script."""
    vs.DSelectAll()
    
    # Créer un rectangle
    rect = create_rectangle(0, 0, DEFAULT_SIZE, DEFAULT_SIZE)
    vs.SetSelect(rect)
    
    # Afficher un message
    vs.Message("Rectangle créé avec succès!")

# Exécuter le script
if __name__ == "__main__":
    main()
```

---

## 🔍 Dépannage

### Le script ne s'exécute pas

- ✅ Vérifiez que Python est activé dans les préférences
- ✅ Assurez-vous qu'il n'y a pas d'erreurs de syntaxe
- ✅ Vérifiez que toutes les fonctions utilisées existent dans le module `vs`
- ✅ Consultez les messages d'erreur dans la console

### Le script ne fait rien

- ✅ Vérifiez que le script est bien exécuté (ajoutez un `print` au début)
- ✅ Assurez-vous que les objets sont créés dans la bonne couche
- ✅ Vérifiez que les coordonnées sont valides

### Erreur "Module not found"

- ✅ Vérifiez que le module est bien `vs` et non `vectorworks` ou autre
- ✅ Assurez-vous que vous utilisez bien l'éditeur de scripts de Vectorworks
- ✅ Si vous utilisez des bibliothèques externes, vérifiez qu'elles sont installées

### Problèmes avec les objets

- ✅ Vérifiez que les handles ne sont pas `None`
- ✅ Assurez-vous que les objets existent avant de les modifier
- ✅ Vérifiez que vous utilisez les bonnes fonctions pour le type d'objet

---

## 📚 Documentation utile

- [Python Scripting Guide](https://developer.vectorworks.net/python) - Guide officiel
- [Python API Reference](https://developer.vectorworks.net/python/api) - Référence de l'API
- [Python vs Module](https://developer.vectorworks.net/python/vs-module) - Documentation du module vs
- [Python Standard Library](https://docs.python.org/3/) - Documentation Python standard

---

## 🎯 Prochaines étapes

1. **Expérimentez** avec les exemples fournis
2. **Modifiez** les scripts pour comprendre leur fonctionnement
3. **Créez** vos propres scripts pour automatiser des tâches
4. **Explorez** la documentation du module `vs` pour découvrir plus de fonctions
5. **Essayez des bibliothèques externes** comme NumPy pour des calculs avancés
6. **Passez au C++** si vous avez besoin de performances ou de fonctionnalités avancées

---

## 📜 Licence

Ces exemples sont sous licence **MIT**. Vous êtes libre de les utiliser, les modifier et les distribuer.

---

*Dernière mise à jour : Août 2024*
*Compatibilité : Vectorworks 2021+*
