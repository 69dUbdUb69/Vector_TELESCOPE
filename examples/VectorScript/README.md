# 📜 VectorScript Example

Ce dossier contient des exemples de scripts **VectorScript** pour Vectorworks. VectorScript est le langage de script historique de Vectorworks, basé sur Pascal. Il permet d'automatiser des tâches, de créer des objets personnalisés et d'étendre les fonctionnalités de Vectorworks sans avoir besoin de compiler du code.

---

## 📚 Ce que vous allez apprendre

✅ Syntaxe de base de VectorScript
✅ Création de procédures et fonctions
✅ Manipulation d'objets Vectorworks
✅ Automatisation de tâches répétitives
✅ Utilisation de l'éditeur de scripts intégré

---

## 🎯 Avantages et Inconvénients

### ✅ Avantages de VectorScript

- **Pas de compilation nécessaire** : Les scripts sont interprétés à la volée
- **Développement rapide** : Idéal pour prototyper des idées
- **Accès complet à l'API Vectorworks** : Toutes les fonctionnalités sont disponibles
- **Portabilité** : Les scripts fonctionnent sur Windows et macOS
- **Éditeur intégré** : Vectorworks inclut un éditeur de scripts avec coloration syntaxique

### ❌ Inconvénients de VectorScript

- **Syntaxe datée** : Basé sur Pascal, moins intuitif que les langages modernes
- **Pas de typage fort** : Peu de vérification à la compilation
- **Performances limitées** : Plus lent que le C++ pour les opérations complexes
- **Gestion de la mémoire manuelle** : Pas de garbage collection
- **Moins de bibliothèques** : Pas d'accès aux bibliothèques externes

---

## 🛠️ Prérequis

- ✅ Vectorworks 2021+ installé
- ✅ Aucun autre outil nécessaire (pas besoin du SDK)

---

## 🚀 Utilisation de VectorScript dans Vectorworks

### 1️⃣ Ouvrir l'éditeur de scripts

1. Dans Vectorworks, allez dans **Outils > Scripts > Éditeur de Scripts**
2. Ou utilisez le raccourci **Ctrl+Shift+S** (Windows) / **Cmd+Shift+S** (macOS)

### 2️⃣ Créer un nouveau script

1. Cliquez sur **Nouveau** dans l'éditeur de scripts
2. Sélectionnez **VectorScript** comme langage
3. Donnez un nom à votre script
4. Commencez à coder !

### 3️⃣ Exécuter un script

- Cliquez sur **Exécuter** (▶️) ou appuyez sur **F5**
- Ou cliquez sur **Exécuter le Script** dans le menu

### 4️⃣ Enregistrer un script

- Cliquez sur **Enregistrer** pour sauvegarder votre script
- Les scripts sont sauvegardés avec l'extension `.vsm`

---

## 📁 Exemples fournis

### 1. [HelloWorld.vsm](HelloWorld.vsm)

Le script le plus simple : affiche une boîte de dialogue avec "Hello, Vectorworks!"

**Code :**
```pascalscript
PROCEDURE HelloWorld;
BEGIN
    Message("Hello, Vectorworks!");
END;
RUN(HelloWorld);
```

---

### 2. [DrawShapes.vsm](DrawShapes.vsm)

Dessine différentes formes géométriques (ligne, cercle, rectangle, polygone).

**Fonctionnalités :**
- Dessine une ligne rouge
- Dessine un cercle bleu
- Dessine un rectangle vert
- Dessine un polygone jaune à 5 côtés

**Code :**
```pascalscript
PROCEDURE DrawShapes;
VAR
    h1, h2, h3, h4 : HANDLE;
BEGIN
    { Dessiner une ligne }
    h1 := Line(0, 0, 100, 100);
    SetColor(h1, 255, 0, 0); { Rouge }
    
    { Dessiner un cercle }
    h2 := Circle(200, 0, 50);
    SetColor(h2, 0, 0, 255); { Bleu }
    
    { Dessiner un rectangle }
    h3 := Rect(0, -100, 100, -50);
    SetColor(h3, 0, 255, 0); { Vert }
    
    { Dessiner un polygone }
    h4 := Polygon(5, 200, -100, 50);
    SetColor(h4, 255, 255, 0); { Jaune }
END;
RUN(DrawShapes);
```

---

### 3. [CreateWall.vsm](CreateWall.vsm)

Crée un mur avec des paramètres personnalisables.

**Fonctionnalités :**
- Crée un mur rectiligne
- Définit la hauteur, l'épaisseur et le matériau
- Positionne le mur à une position spécifique

**Code :**
```pascalscript
PROCEDURE CreateWall;
VAR
    wallHandle : HANDLE;
    startX, startY : REAL;
    length : REAL;
    height : REAL;
    thickness : REAL;
BEGIN
    { Position de départ }
    startX := 0;
    startY := 0;
    
    { Dimensions du mur }
    length := 5000; { 5 mètres }
    height := 3000; { 3 mètres }
    thickness := 200; { 20 cm }
    
    { Créer le mur }
    wallHandle := Wall(startX, startY, length, height, thickness);
    
    { Définir le matériau }
    SetWallMaterial(wallHandle, 'Brique');
    
    { Définir la couleur }
    SetColor(wallHandle, 200, 100, 50); { Marron }
END;
RUN(CreateWall);
```

---

### 4. [SelectAndModify.vsm](SelectAndModify.vsm)

Sélectionne tous les objets d'un certain type et les modifie.

**Fonctionnalités :**
- Sélectionne tous les cercles dans le document
- Change leur couleur en rouge
- Change leur rayon à 100mm

**Code :**
```pascalscript
PROCEDURE SelectAndModify;
VAR
    h : HANDLE;
    radius : REAL;
BEGIN
    { Désélectionner tout }
    DSelectAll;
    
    { Sélectionner tous les cercles }
    h := FSActLayer;
    While (h <> Nil) Do BEGIN
        If (GetType(h) = 3) Then BEGIN { 3 = type Circle }
            SetSelect(h);
        END;
        h := NextObj(h);
    END;
    
    { Modifier les cercles sélectionnés }
    h := FSActLayer;
    While (h <> Nil) Do BEGIN
        If (GetSelect(h)) Then BEGIN
            { Changer la couleur }
            SetColor(h, 255, 0, 0); { Rouge }
            
            { Changer le rayon }
            radius := 100;
            SetRadius(h, radius);
        END;
        h := NextObj(h);
    END;
    
    { Rafraîchir l'affichage }
    UpdateDisplay;
END;
RUN(SelectAndModify);
```

---

### 5. [ParametricObject.vsm](ParametricObject.vsm)

Crée un objet paramétrique simple avec une boîte de dialogue.

**Fonctionnalités :**
- Affiche une boîte de dialogue pour demander les dimensions
- Crée un rectangle avec les dimensions spécifiées
- Montre comment utiliser les boîtes de dialogue

**Code :**
```pascalscript
PROCEDURE ParametricObject;
VAR
    width, height : REAL;
    rectHandle : HANDLE;
    result : BOOLEAN;
BEGIN
    { Afficher une boîte de dialogue pour demander les dimensions }
    result := GetReal("Largeur (mm)", width, 100);
    If (result) Then BEGIN
        result := GetReal("Hauteur (mm)", height, 100);
        If (result) Then BEGIN
            { Créer un rectangle avec les dimensions spécifiées }
            rectHandle := Rect(0, 0, width, height);
            
            { Définir la couleur }
            SetColor(rectHandle, 0, 100, 200);
            
            Message("Rectangle créé avec succès!");
        END;
    END;
END;
RUN(ParametricObject);
```

---

### 6. [BatchRename.vsm](BatchRename.vsm)

Renomme plusieurs objets en une seule fois.

**Fonctionnalités :**
- Demande un préfixe à l'utilisateur
- Renomme tous les objets sélectionnés avec ce préfixe
- Ajoute un numéro séquentiel

**Code :**
```pascalscript
PROCEDURE BatchRename;
VAR
    h : HANDLE;
    prefix : STRING;
    count : INTEGER;
    newName : STRING;
BEGIN
    { Demander le préfixe }
    If (GetString("Préfixe pour le renommage", prefix)) Then BEGIN
        count := 1;
        h := FSActLayer;
        
        { Parcourir tous les objets }
        While (h <> Nil) Do BEGIN
            If (GetSelect(h)) Then BEGIN
                { Créer un nouveau nom }
                newName := Concat(prefix, ' ', Num2Str(0, count));
                
                { Renommer l'objet }
                SetName(h, newName);
                
                count := count + 1;
            END;
            h := NextObj(h);
        END;
        
        Message(Concat(Num2Str(0, count - 1), ' objets renommés'));
    END;
END;
RUN(BatchRename);
```

---

## 🔧 Syntaxe de VectorScript

### Types de données

| Type | Description | Exemple |
|------|-------------|---------|
| `REAL` | Nombre décimal | `100.5` |
| `INTEGER` | Nombre entier | `42` |
| `BOOLEAN` | Booléen | `TRUE`, `FALSE` |
| `STRING` | Chaîne de caractères | `'Bonjour'` |
| `HANDLE` | Référence à un objet | `h := Line(0, 0, 10, 10)` |
| `POINT` | Point 2D | `pt := (10, 20)` |

---

### Variables

```pascalscript
VAR
    x, y : REAL;       { Déclaration de variables réelles }
    count : INTEGER;   { Déclaration d'une variable entière }
    name : STRING;     { Déclaration d'une chaîne }
    h : HANDLE;        { Déclaration d'une référence d'objet }
```

---

### Structures de contrôle

#### Condition IF

```pascalscript
If (condition) Then BEGIN
    { code à exécuter si condition est vraie }
END
Else BEGIN
    { code à exécuter sinon }
END;
```

#### Boucle WHILE

```pascalscript
While (condition) Do BEGIN
    { code à exécuter tant que condition est vraie }
END;
```

#### Boucle FOR

```pascalscript
FOR i := 1 TO 10 Do BEGIN
    { code à exécuter 10 fois }
END;
```

---

### Procédures et Fonctions

#### Procédure (sans valeur de retour)

```pascalscript
PROCEDURE MaProcedure;
VAR
    x : REAL;
BEGIN
    { code }
END;
```

#### Fonction (avec valeur de retour)

```pascalscript
FUNCTION MaFonction(param : REAL) : REAL;
BEGIN
    MaFonction := param * 2; { Retourne la valeur }
END;
```

---

### Fonctions utiles

#### Affichage

```pascalscript
Message("Mon message");           { Boîte de dialogue simple }
Alert("Attention!", "Message");   { Boîte de dialogue avec titre }
```

#### Entrées utilisateur

```pascalscript
GetReal("Largeur", valeur, 100.0);    { Demande un nombre réel }
GetInteger("Nombre", valeur, 1);     { Demande un entier }
GetString("Nom", texte, "");         { Demande une chaîne }
GetBoolean("Activer?", valeur, TRUE); { Demande un booléen }
```

#### Création d'objets

```pascalscript
Line(x1, y1, x2, y2)          { Ligne }
Circle(x, y, rayon)          { Cercle }
Rect(x1, y1, x2, y2)          { Rectangle }
Polygon(nbCotes, x, y, rayon){ Polygone régulier }
Arc(x, y, rayon, angle1, angle2) { Arc de cercle }
Text(x, y, texte)            { Texte }
Wall(x, y, longueur, hauteur, epaisseur) { Mur }
```

#### Manipulation d'objets

```pascalscript
SetSelect(h)             { Sélectionne un objet }
DSelect(h)               { Désélectionne un objet }
DSelectAll               { Désélectionne tout }
SetColor(h, r, v, b)    { Définit la couleur }
SetPenColor(h, r, v, b) { Définit la couleur du contour }
SetFillColor(h, r, v, b){ Définit la couleur de remplissage }
Move(h, dx, dy)         { Déplace un objet }
Rotate(h, angle)        { Tourne un objet }
Scale(h, facteur)       { Redimensionne un objet }
Delete(h)               { Supprime un objet }
```

#### Accès aux propriétés

```pascalscript
GetType(h)              { Retourne le type de l'objet }
GetX(h)                { Retourne la position X }
GetY(h)                { Retourne la position Y }
GetRadius(h)           { Retourne le rayon (pour un cercle) }
GetWidth(h)            { Retourne la largeur }
GetHeight(h)           { Retourne la hauteur }
GetName(h)             { Retourne le nom de l'objet }
GetSelect(h)           { Retourne TRUE si l'objet est sélectionné }
```

---

## 🎨 Bonnes pratiques

### 1. Commenter votre code

```pascalscript
{ Ceci est un commentaire sur une ligne }

{ Ceci est un commentaire
   sur plusieurs lignes }
```

### 2. Gérer les erreurs

```pascalscript
h := Line(0, 0, 10, 10);
If (h = Nil) Then BEGIN
    Message("Erreur : Impossible de créer la ligne!");
END;
```

### 3. Utiliser des constantes

```pascalscript
CONST
    kPi = 3.14159;
    kDefaultWidth = 100.0;
    kDefaultColorRed = 255;
```

### 4. Structurer votre code

```pascalscript
{ Déclarations }
CONST
    kMaxIterations = 100;

VAR
    i : INTEGER;
    h : HANDLE;

{ Fonctions }
FUNCTION CalculateArea(width, height : REAL) : REAL;
BEGIN
    CalculateArea := width * height;
END;

{ Procédure principale }
PROCEDURE Main;
BEGIN
    { Appel de la fonction }
    Message(Concat('Area: ', Num2Str(0, CalculateArea(10, 20))));
END;

{ Exécution }
RUN(Main);
```

---

## 🔍 Dépannage

### Le script ne s'exécute pas

- ✅ Vérifiez qu'il n'y a pas d'erreurs de syntaxe
- ✅ Assurez-vous que toutes les variables sont déclarées
- ✅ Vérifiez que les parenthèses et points-virgules sont corrects
- ✅ Consultez les messages d'erreur dans l'éditeur de scripts

### Le script ne fait rien

- ✅ Vérifiez que `RUN(nomDeLaProcedure)` est appelé à la fin
- ✅ Assurez-vous que les objets sont créés dans la bonne couche
- ✅ Vérifiez que les coordonnées sont valides

### Erreur "Unknown identifier"

- ✅ Vérifiez l'orthographe de la fonction ou variable
- ✅ Assurez-vous que la variable est déclarée avant d'être utilisée
- ✅ Vérifiez que vous utilisez la bonne casse (VectorScript est sensible à la casse)

### Problèmes de sélection

- ✅ Utilisez `FSActLayer` pour parcourir tous les objets de la couche active
- ✅ Utilisez `NextObj(h)` pour obtenir l'objet suivant
- ✅ Vérifiez que les objets existent avec `h <> Nil`

---

## 📚 Documentation utile

- [VectorScript Reference](https://developer.vectorworks.net/vectorscript) - Référence complète
- [VectorScript Cookbook](https://developer.vectorworks.net/vectorscript/cookbook) - Recettes et exemples
- [VectorScript Functions](https://developer.vectorworks.net/vectorscript/functions) - Liste complète des fonctions
- [VectorScript Types](https://developer.vectorworks.net/vectorscript/types) - Types de données et objets

---

## 🎯 Prochaines étapes

1. **Expérimentez** avec les exemples fournis
2. **Modifiez** les scripts pour comprendre leur fonctionnement
3. **Créez** vos propres scripts pour automatiser des tâches
4. **Explorez** la documentation officielle pour découvrir plus de fonctions
5. **Passez à Python** si vous voulez un langage plus moderne
6. **Passez au C++** si vous avez besoin de performances ou de fonctionnalités avancées

---

## 📜 Licence

Ces exemples sont sous licence **MIT**. Vous êtes libre de les utiliser, les modifier et les distribuer.

---

*Dernière mise à jour : Août 2024*
*Compatibilité : Vectorworks 2021+*
