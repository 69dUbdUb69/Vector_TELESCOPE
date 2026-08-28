# ⚡ CustomCommand Plugin

Le plugin **CustomCommand** montre comment créer une **commande personnalisée** dans Vectorworks. Contrairement aux Plug-in Objects (PIO) qui créent des objets dans le dessin, les commandes personnalisées exécutent des actions quand elles sont appelées depuis le menu ou via un raccourci clavier.

---

## 📚 Ce que vous allez apprendre

✅ Créer des commandes personnalisées
✅ Enregistrer une commande auprès de Vectorworks
✅ Exécuter du code quand la commande est appelée
✅ Accéder à la sélection actuelle
✅ Modifier des objets existants
✅ Gérer l'état activé/désactivé d'une commande

---

## 🎯 Fonctionnalités

Ce plugin crée une commande qui :
- S'affiche dans le menu **Outils > Plugins**
- Est activée uniquement quand des objets sont sélectionnés
- Affiche un message avec le nombre d'objets sélectionnés
- Peut être assignée à un raccourci clavier

---

## 📁 Structure du projet

```
CustomCommand/
├── src/
│   ├── CustomCommand.cpp   # Code principal
│   └── CustomCommand.h     # Déclarations
├── CMakeLists.txt           # Configuration CMake
└── README.md                # Ce fichier
```

---

## 🛠️ Prérequis

- ✅ [Vectorworks 2021+](https://www.vectorworks.net) installé
- ✅ [Le SDK Vectorworks](https://developer.vectorworks.net) téléchargé
- ✅ Un compilateur C++ (Visual Studio 2019+ ou Xcode 14+)

---

## 🚀 Étapes pour créer le plugin

### 1️⃣ Comprendre les différences avec les PIO

| Caractéristique | Plug-in Object (PIO) | Commande Personnalisée |
|----------------|---------------------|------------------------|
| **Type** | Objet dans le dessin | Action exécutée |
| **Classe de base** | `VWPlugInObject` | `VWPlugInCommand` |
| **Enregistrement** | `VS_RegisterObject` | `VS_RegisterCommand` |
| **Fonction principale** | `Recalculate()` | `Execute()` |
| **Accès à la sélection** | Non | Oui |
| **Géométrie** | Oui | Non (sauf création d'objets) |

---

### 2️⃣ Examiner le code

#### Fichier `CustomCommand.h`

```cpp
#ifndef CUSTOMCOMMAND_H
#define CUSTOMCOMMAND_H

#include <VS_PlugIn.h>

class CustomCommand : public VWPlugInCommand {
public:
    CustomCommand();
    virtual ~CustomCommand();
    
    // Méthodes virtuelles
    virtual VWErrorCode Init() override;
    virtual VWErrorCode Execute() override;
    virtual bool IsEnabled() override;
    
    // Identification
    static const char* GetPlugInName();
    static const char* GetPlugInDisplayName();
    static VWPlugInID GetPlugInID();
    
private:
    static const TXString kPlugInID;
};

#endif // CUSTOMCOMMAND_H
```

**Différences avec HelloWorld :**
- On hérite de `VWPlugInCommand` au lieu de `VWPlugInObject`
- On implémente `Execute()` au lieu de `Recalculate()`
- On implémente `IsEnabled()` pour gérer l'état de la commande

---

#### Fichier `CustomCommand.cpp`

Le fichier contient :
1. L'initialisation et l'enregistrement de la commande
2. La méthode `Execute()` qui contient la logique de la commande
3. La méthode `IsEnabled()` qui détermine si la commande est active

---

### 3️⃣ Examiner la fonction Init

```cpp
VWErrorCode CustomCommand::Init() {
    VS_OutputDebugString("CustomCommand: Init appelée\n");
    
    // Enregistrer la commande auprès de Vectorworks
    VWErrorCode err = VS_RegisterCommand(
        GetPlugInName(),
        GetPlugInDisplayName(),
        kVWCommandCategoryCustom,
        this
    );
    
    if (err != kVWNoError) {
        VS_OutputDebugString("Erreur lors de l'enregistrement de la commande\n");
    }
    
    return err;
}
```

**Explications :**
- `VS_RegisterCommand` enregistre la commande
- `kVWCommandCategoryCustom` : La commande apparaît dans **Outils > Plugins > Custom**
- Autres catégories possibles :
  - `kVWCommandCategoryFile` : Menu Fichier
  - `kVWCommandCategoryEdit` : Menu Édition
  - `kVWCommandCategoryView` : Menu Affichage
  - `kVWCommandCategoryTools` : Menu Outils

---

### 4️⃣ Examiner la fonction Execute

```cpp
VWErrorCode CustomCommand::Execute() {
    VS_OutputDebugString("CustomCommand: Execute appelée\n");
    
    // Compter le nombre d'objets sélectionnés
    VWObjectIterator iter(kVWSelectionSetActive);
    VWObjectHandle hObj;
    int count = 0;
    
    while (iter.Next(hObj)) {
        count++;
    }
    
    // Afficher un message avec le nombre d'objets sélectionnés
    TXString message = TXString::Format(
        "Commande personnalisée exécutée !\nNombre d'objets sélectionnés : %d",
        count
    );
    
    // Afficher le message dans une boîte de dialogue
    VS_Alert(message, kVWAlertOK, kVWAlertNote);
    
    // Exemple : Modifier les objets sélectionnés
    if (count > 0) {
        // Réinitialiser l'itérateur
        iter.Reset();
        
        // Parcourir à nouveau les objets sélectionnés
        while (iter.Next(hObj)) {
            // Changer la couleur de chaque objet sélectionné
            VWColor newColor(0, 255, 0); // Vert
            VS_SetObjectColor(hObj, newColor);
        }
        
        // Mettre à jour l'affichage
        VS_UpdateDisplay();
    }
    
    return kVWNoError;
}
```

**Explications :**
1. **Accéder à la sélection** : `VWObjectIterator` permet de parcourir les objets sélectionnés
2. **Compter les objets** : On utilise `iter.Next(hObj)` pour obtenir chaque objet
3. **Afficher un message** : `VS_Alert` affiche une boîte de dialogue
4. **Modifier des objets** : `VS_SetObjectColor` change la couleur d'un objet
5. **Mettre à jour l'affichage** : `VS_UpdateDisplay()` rafraîchit l'affichage

---

### 5️⃣ Examiner la fonction IsEnabled

```cpp
bool CustomCommand::IsEnabled() {
    // La commande est activée s'il y a au moins un objet sélectionné
    VWObjectIterator iter(kVWSelectionSetActive);
    return iter.HasNext();
}
```

**Explications :**
- `IsEnabled()` est appelée par Vectorworks pour déterminer si la commande doit être activée
- Retourne `true` si la commande peut être exécutée, `false` sinon
- Dans cet exemple, la commande est activée uniquement s'il y a des objets sélectionnés

---

### 6️⃣ Compiler et déployer

Suivez les mêmes étapes que pour les exemples précédents :

1. Configurez votre environnement (VW_SDK_PATH)
2. Créez le projet avec CMake ou manuellement
3. Compilez en mode Release
4. Copiez le fichier `CustomCommand.vso` dans le dossier Plug-ins de Vectorworks
5. Redémarrez Vectorworks

---

### 7️⃣ Tester le plugin

1. Lancez Vectorworks
2. Dessinez quelques objets (lignes, cercles, etc.)
3. Sélectionnez un ou plusieurs objets
4. Dans le menu **Outils > Plugins**, vous devriez voir **Custom Command**
5. La commande devrait être **activée** (non grisée)
6. Cliquez sur la commande
7. Une boîte de dialogue devrait s'afficher avec le nombre d'objets sélectionnés
8. Les objets sélectionnés devraient devenir **verts**

> 🎉 **Félicitations !** Votre première commande personnalisée fonctionne !

---

## 🎨 Personnalisation

### Changer le comportement de la commande

Pour faire autre chose que changer la couleur :

```cpp
// Déplacer les objets sélectionnés de 10mm vers la droite
while (iter.Next(hObj)) {
    VWPoint3D currentPos;
    VS_GetObjectPosition(hObj, currentPos);
    
    VWPoint3D newPos(currentPos.x + 10, currentPos.y, currentPos.z);
    VS_SetObjectPosition(hObj, newPos);
}
```

### Ajouter des paramètres à la commande

Les commandes peuvent aussi avoir des paramètres qui s'affichent dans une boîte de dialogue :

```cpp
// Dans Init()
VWErrorCode CustomCommand::Init() {
    // ... enregistrement de la commande ...
    
    // Ajouter un paramètre pour la distance de déplacement
    AddParam("Distance", kVWParamTypeReal, kVWParamOptReadWrite, 10.0);
    
    return kVWNoError;
}

// Dans Execute()
VWErrorCode CustomCommand::Execute() {
    double distance;
    GetParamReal(0, distance); // Récupérer la valeur du paramètre
    
    VWObjectIterator iter(kVWSelectionSetActive);
    VWObjectHandle hObj;
    
    while (iter.Next(hObj)) {
        VWPoint3D currentPos;
        VS_GetObjectPosition(hObj, currentPos);
        
        VWPoint3D newPos(currentPos.x + distance, currentPos.y, currentPos.z);
        VS_SetObjectPosition(hObj, newPos);
    }
    
    return kVWNoError;
}
```

---

## 🔍 Dépannage

### La commande n'apparaît pas dans le menu

- ✅ Vérifiez que `VS_RegisterCommand` est appelée dans `Init()`
- ✅ Assurez-vous que `Init()` retourne `kVWNoError`
- ✅ Vérifiez que le fichier `.vso` est dans le bon dossier
- ✅ Redémarrez Vectorworks

### La commande est grisée

- ✅ Vérifiez que `IsEnabled()` retourne `true` dans les cas appropriés
- ✅ Assurez-vous qu'il y a bien des objets sélectionnés (pour cet exemple)

### La commande ne fait rien

- ✅ Vérifiez que `Execute()` est appelée (ajoutez un `VS_OutputDebugString`)
- ✅ Assurez-vous que la sélection n'est pas vide
- ✅ Vérifiez que vous utilisez les bonnes fonctions API

---

## 🎯 Prochaines étapes

Maintenant que vous maîtrisez les commandes personnalisées, vous pouvez :

1. **[Créer des commandes plus complexes](https://developer.vectorworks.net/api/group___v_w___commands.html)**
2. **[Ajouter des boîtes de dialogue personnalisées](https://developer.vectorworks.net/api/class_v_w_dialog.html)**
3. **[Créer des palettes d'outils personnalisées](https://developer.vectorworks.net/api/group___v_w___tools.html)**
4. **[Combiner PIO et commandes](https://developer.vectorworks.net/guides/combining-pio-and-commands)**

---

## 📚 Documentation utile

- [API Reference - VWPlugInCommand](https://developer.vectorworks.net/api/class_v_w_plug_in_command.html)
- [API Reference - VS_RegisterCommand](https://developer.vectorworks.net/api/group___v_w___registration.html)
- [API Reference - VWObjectIterator](https://developer.vectorworks.net/api/class_v_w_object_iterator.html)
- [Guide des commandes personnalisées](https://developer.vectorworks.net/guides/custom-commands)

---

## 📜 Licence

Ce code est sous licence **MIT**. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

*Dernière mise à jour : Août 2024*
*Compatibilité : Vectorworks 2021+*
