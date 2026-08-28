# 📦 ParametricBox Plugin

Le plugin **ParametricBox** est un exemple avancé qui montre comment créer un **objet paramétrique 3D** dans Vectorworks. Contrairement à l'exemple HelloWorld qui affiche simplement du texte, ce plugin crée une boîte 3D dont les dimensions peuvent être modifiées via la palette d'information (OIP).

---

## 📚 Ce que vous allez apprendre

✅ Créer des objets paramétriques avec des paramètres éditables
✅ Utiliser la palette d'information (OIP) pour interagir avec l'utilisateur
✅ Créer de la géométrie 3D (extrusions, faces, etc.)
✅ Gérer les mises à jour de l'objet quand les paramètres changent
✅ Organiser le code d'un plugin plus complexe

---

## 🎯 Fonctionnalités

- **Paramètres personnalisables** : Largeur, Hauteur, Profondeur
- **Géométrie 3D** : Création d'une boîte 3D avec extrusion
- **Visualisation en temps réel** : La boîte se met à jour quand les paramètres changent
- **Couleurs personnalisables** : Couleur de la boîte modifiable

---

## 📁 Structure du projet

```
ParametricBox/
├── src/
│   ├── ParametricBox.cpp      # Code principal
│   └── ParametricBox.h        # Déclarations
├── CMakeLists.txt             # Configuration CMake
└── README.md                  # Ce fichier
```

---

## 🛠️ Prérequis

- ✅ [Vectorworks 2021+](https://www.vectorworks.net) installé
- ✅ [Le SDK Vectorworks](https://developer.vectorworks.net) téléchargé
- ✅ Un compilateur C++ (Visual Studio 2019+ ou Xcode 14+)
- ✅ CMake 3.20+ (optionnel)

---

## 🚀 Étapes pour créer le plugin

### 1️⃣ Comprendre le code

#### Fichier `ParametricBox.h`

```cpp
#ifndef PARAMETRICBOX_H
#define PARAMETRICBOX_H

#include <VS_PlugIn.h>

class ParametricBox : public VWPlugInObject {
public:
    ParametricBox();
    virtual ~ParametricBox();
    
    // Méthodes virtuelles
    virtual VWErrorCode Init() override;
    virtual VWErrorCode Recalculate() override;
    
    // Identification
    static const char* GetPlugInName();
    static const char* GetPlugInDisplayName();
    static VWPlugInID GetPlugInID();
    
private:
    static const TXString kPlugInID;
    
    // Index des paramètres (pour un accès plus rapide)
    enum ParamIndex {
        kParamWidth = 0,
        kParamHeight,
        kParamDepth,
        kParamColor
    };
};

#endif // PARAMETRICBOX_H
```

**Nouveautés par rapport à HelloWorld :**
- Déclaration d'un `enum` pour gérer les index des paramètres
- Cela permet d'accéder plus facilement aux paramètres par leur index

---

#### Fichier `ParametricBox.cpp`

Le fichier contient plusieurs parties importantes :

1. **Initialisation des paramètres** dans `Init()`
2. **Récupération des valeurs** dans `Recalculate()`
3. **Création de la géométrie 3D**

---

### 2️⃣ Examiner la fonction Init

```cpp
VWErrorCode ParametricBox::Init() {
    VS_OutputDebugString("ParametricBox: Init appelée\n");
    
    // Enregistrer l'objet
    VWErrorCode err = VS_RegisterObject(
        GetPlugInName(),
        GetPlugInDisplayName(),
        kVWObjectTypeCustom,
        this
    );
    
    if (err != kVWNoError) {
        return err;
    }
    
    // Ajouter les paramètres
    // Largeur (paramètre numérique avec valeur par défaut 100mm)
    AddParam("Largeur", kVWParamTypeReal, kVWParamOptReadWrite, 100.0);
    
    // Hauteur
    AddParam("Hauteur", kVWParamTypeReal, kVWParamOptReadWrite, 100.0);
    
    // Profondeur
    AddParam("Profondeur", kVWParamTypeReal, kVWParamOptReadWrite, 100.0);
    
    // Couleur (paramètre couleur)
    AddParam("Couleur", kVWParamTypeColor, kVWParamOptReadWrite, VWColor(255, 0, 0));
    
    return kVWNoError;
}
```

**Explications :**
- `AddParam()` permet d'ajouter un paramètre à l'objet
- **Types de paramètres** :
  - `kVWParamTypeReal` : Nombre décimal (pour les dimensions)
  - `kVWParamTypeInteger` : Nombre entier
  - `kVWParamTypeString` : Texte
  - `kVWParamTypeBool` : Booléen (case à cocher)
  - `kVWParamTypeColor` : Couleur
  - `kVWParamTypePopup` : Liste déroulante
- **Options** :
  - `kVWParamOptReadWrite` : Lecture/écriture (modifiable par l'utilisateur)
  - `kVWParamOptReadOnly` : Lecture seule
  - `kVWParamOptHidden` : Masqué (non visible dans l'OIP)

---

### 3️⃣ Examiner la fonction Recalculate

```cpp
VWErrorCode ParametricBox::Recalculate() {
    VS_OutputDebugString("ParametricBox: Recalculate appelée\n");
    
    // Effacer la géométrie existante
    ClearObjects();
    
    // Récupérer les valeurs des paramètres
    double largeur, hauteur, profondeur;
    VWColor couleur;
    
    GetParamReal(kParamWidth, largeur);
    GetParamReal(kParamHeight, hauteur);
    GetParamReal(kParamDepth, profondeur);
    GetParamColor(kParamColor, couleur);
    
    // Créer la géométrie 2D de base (un rectangle)
    VWRect2D rect(
        -largeur / 2, -profondeur / 2,  // Coin inférieur gauche
        largeur / 2, profondeur / 2    // Coin supérieur droit
    );
    
    // Créer un polygone à partir du rectangle
    VWPolygon2D polygon;
    polygon.AddVertex(rect.GetMinX(), rect.GetMinY());
    polygon.AddVertex(rect.GetMaxX(), rect.GetMinY());
    polygon.AddVertex(rect.GetMaxX(), rect.GetMaxY());
    polygon.AddVertex(rect.GetMinX(), rect.GetMaxY());
    polygon.SetClosed(true);
    
    // Extruder le polygone pour créer une boîte 3D
    VWExtrude extrude;
    extrude.SetBasePolygon(polygon);
    extrude.SetExtrusionVector(VWPoint3D(0, 0, hauteur));
    extrude.SetExtrusionType(kVWExtrusionTypeVertical);
    
    // Définir la couleur
    extrude.SetPenColor(couleur);
    extrude.SetFillColor(couleur);
    
    // Ajouter l'extrusion au modèle
    AddExtrude(extrude);
    
    return kVWNoError;
}
```

**Explications :**
1. **Récupération des paramètres** : On utilise `GetParamReal()` et `GetParamColor()` pour récupérer les valeurs actuelles
2. **Création de la géométrie 2D** : On crée un rectangle centré sur l'origine
3. **Création du polygone** : On convertit le rectangle en polygone (nécessaire pour l'extrusion)
4. **Extrusion** : On extrude le polygone 2D pour créer un objet 3D
5. **Couleurs** : On définit la couleur du contour et du remplissage
6. **Ajout au modèle** : `AddExtrude()` ajoute l'objet 3D au modèle

---

### 4️⃣ Compiler et déployer

Suivez les mêmes étapes que pour l'exemple [HelloWorld](../HelloWorld/README.md) :

1. Configurez votre environnement (VW_SDK_PATH)
2. Créez le projet avec CMake ou manuellement
3. Compilez en mode Release
4. Copiez le fichier `ParametricBox.vso` dans le dossier Plug-ins de Vectorworks
5. Redémarrez Vectorworks

---

### 5️⃣ Tester le plugin

1. Lancez Vectorworks
2. Dans le menu **Outils > Plugins**, sélectionnez **Parametric Box**
3. Cliquez dans votre document pour placer la boîte
4. Ouvrez la **palette d'information (OIP)** (F4 ou menu Fenêtre > Palette d'information)
5. Modifiez les valeurs de **Largeur**, **Hauteur** et **Profondeur**
6. La boîte devrait se mettre à jour en temps réel !

> 🎉 **Félicitations !** Vous avez créé votre premier objet paramétrique 3D !

---

## 🎨 Personnalisation

### Ajouter un nouveau paramètre

Pour ajouter un paramètre (par exemple, un rayon pour les coins arrondis) :

1. Ajoutez l'index dans l'enum :
   ```cpp
   enum ParamIndex {
       kParamWidth = 0,
       kParamHeight,
       kParamDepth,
       kParamColor,
       kParamCornerRadius  // Nouveau
   };
   ```

2. Ajoutez le paramètre dans `Init()` :
   ```cpp
   AddParam("Rayon des coins", kVWParamTypeReal, kVWParamOptReadWrite, 0.0);
   ```

3. Utilisez-le dans `Recalculate()` :
   ```cpp
   double cornerRadius;
   GetParamReal(kParamCornerRadius, cornerRadius);
   // Utilisez cornerRadius pour créer des coins arrondis
   ```

---

### Changer la géométrie

Pour créer une forme différente (par exemple, un cylindre) :

```cpp
// Créer un cercle
VWCircle2D circle(VWPoint2D(0, 0), largeur / 2);

// Extruder le cercle
VWExtrude extrude;
extrude.SetBaseCircle(circle);
extrude.SetExtrusionVector(VWPoint3D(0, 0, hauteur));
extrude.SetExtrusionType(kVWExtrusionTypeVertical);
extrude.SetPenColor(couleur);
extrude.SetFillColor(couleur);

AddExtrude(extrude);
```

---

## 🔍 Dépannage

### Les paramètres ne s'affichent pas

- ✅ Vérifiez que `AddParam()` est appelée dans `Init()`
- ✅ Assurez-vous que les options incluent `kVWParamOptReadWrite`
- ✅ Vérifiez que `Init()` retourne `kVWNoError`

### La géométrie ne se met pas à jour

- ✅ Vérifiez que `ClearObjects()` est appelée au début de `Recalculate()`
- ✅ Assurez-vous que `GetParam*` est appelée avec les bons index
- ✅ Vérifiez que vous utilisez bien les valeurs récupérées

### Problèmes avec l'extrusion

- ✅ Vérifiez que le polygone est fermé (`SetClosed(true)`)
- ✅ Assurez-vous que le vecteur d'extrusion n'est pas nul
- ✅ Vérifiez que les coordonnées sont valides (pas de NaN)

---

## 🎯 Prochaines étapes

Maintenant que vous maîtrisez les objets paramétriques, vous pouvez :

1. **[Créer des formes plus complexes](https://developer.vectorworks.net/api/class_v_w_polygon3_d.html)** (polygones 3D, surfaces NURBS)
2. **[Ajouter des contraintes](https://developer.vectorworks.net/api/group___v_w___constraints.html)** entre les paramètres
3. **[Créer des objets avec des trous](https://developer.vectorworks.net/api/class_v_w_boolean.html)** (opérations booléennes)
4. **[Explorer les événements](https://developer.vectorworks.net/api/class_v_w_plug_in_object.html#events)** (clics, survol, etc.)

---

## 📚 Documentation utile

- [API Reference - VWPlugInObject](https://developer.vectorworks.net/api/class_v_w_plug_in_object.html)
- [API Reference - VWExtrude](https://developer.vectorworks.net/api/class_v_w_extrude.html)
- [API Reference - VWPolygon2D](https://developer.vectorworks.net/api/class_v_w_polygon2_d.html)
- [Guide des paramètres](https://developer.vectorworks.net/guides/parameters)

---

## 📜 Licence

Ce code est sous licence **MIT**. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

*Dernière mise à jour : Août 2024*
*Compatibilité : Vectorworks 2021+*
