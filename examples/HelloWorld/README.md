# 🌍 HelloWorld Plugin

Le plugin **HelloWorld** est le point de départ idéal pour apprendre à créer des plugins Vectorworks en C++. Il s'agit d'un **Plug-in Object (PIO)** minimal qui affiche simplement un message dans la palette d'information.

---

## 📚 Ce que vous allez apprendre

✅ Structure de base d'un plugin Vectorworks
✅ Configuration du projet (Visual Studio / Xcode)
✅ Enregistrement d'un objet personnalisé
✅ Utilisation de l'API Vectorworks
✅ Compilation et déploiement

---

## 📁 Structure du projet

```
HelloWorld/
├── src/
│   ├── HelloWorld.cpp      # Code principal
│   └── HelloWorld.h        # Déclarations
├── CMakeLists.txt          # Configuration CMake
├── HelloWorld.vcxproj      # Projet Visual Studio (Windows)
├── HelloWorld.xcodeproj    # Projet Xcode (macOS)
└── README.md               # Ce fichier
```

---

## 🛠️ Prérequis

Avant de commencer, assurez-vous d'avoir :

- ✅ [Vectorworks 2021+](https://www.vectorworks.net) installé
- ✅ [Le SDK Vectorworks](https://developer.vectorworks.net) téléchargé et extrait
- ✅ Visual Studio 2019+ (Windows) ou Xcode 14+ (macOS)
- ✅ CMake 3.20+ (optionnel mais recommandé)

---

## 🚀 Étapes pour créer le plugin

### 1️⃣ Configurer l'environnement

#### Définir la variable d'environnement `VW_SDK_PATH`

**Windows (PowerShell)** :
```powershell
$env:VW_SDK_PATH = "C:\Chemin\Vers\Vectorworks_SDK_2024"
```

**macOS (Terminal)** :
```bash
export VW_SDK_PATH="/Applications/Vectorworks 2024/SDK"
```

> 💡 **Astuce** : Pour rendre cette variable permanente, ajoutez-la à votre profil utilisateur.

---

### 2️⃣ Créer le projet

#### Option A : Utiliser CMake (recommandé)

1. Créez un dossier `HelloWorld`
2. Copiez le fichier [`CMakeLists.txt`](CMakeLists.txt) de cet exemple
3. Créez un dossier `src` et copiez-y [`HelloWorld.h`](src/HelloWorld.h) et [`HelloWorld.cpp`](src/HelloWorld.cpp)
4. Configurez et compilez :

**Windows :**
```bash
cd HelloWorld
mkdir build
cd build
cmake .. -G "Visual Studio 17 2022" -A x64
cmake --build . --config Release
```

**macOS :**
```bash
cd HelloWorld
mkdir build
cd build
cmake .. -G Xcode
cmake --build . --config Release
```

#### Option B : Créer un projet manuellement

**Visual Studio (Windows) :**
1. Ouvrez Visual Studio
2. Créez un nouveau projet **Dynamic Link Library (DLL)**
3. Nommez-le `HelloWorld`
4. Configurez les propriétés du projet :
   - **Configuration Type** : Dynamic Library (.dll)
   - **Platform** : x64
   - **Runtime Library** : Multi-threaded DLL (/MD)
5. Ajoutez les chemins du SDK :
   - **Include Directories** : `$VW_SDK_PATH\Include`
   - **Library Directories** : `$VW_SDK_PATH\Lib\Win64`
   - **Additional Dependencies** : `VS_2024.lib` (selon votre version)
6. Ajoutez les fichiers `HelloWorld.h` et `HelloWorld.cpp`

**Xcode (macOS) :**
1. Ouvrez Xcode
2. Créez un nouveau projet **Dynamic Library**
3. Nommez-le `HelloWorld`
4. Configurez le projet :
   - **Product Name** : HelloWorld
   - **Type** : Dynamic Library
   - **Architectures** : x86_64
5. Ajoutez les chemins du SDK dans **Build Settings > Header Search Paths**
6. Ajoutez les bibliothèques dans **Build Phases > Link Binary With Libraries**
7. Ajoutez les fichiers `HelloWorld.h` et `HelloWorld.cpp`

---

### 3️⃣ Examiner le code

#### Fichier `HelloWorld.h`

```cpp
#ifndef HELLOWORLD_H
#define HELLOWORLD_H

#include <VS_PlugIn.h>

class HelloWorld : public VWPlugInObject {
public:
    HelloWorld();
    virtual ~HelloWorld();
    
    // Méthodes virtuelles à implémenter
    virtual VWErrorCode Init() override;
    virtual VWErrorCode Recalculate() override;
    
    // Identification du plugin
    static const char* GetPlugInName();
    static const char* GetPlugInDisplayName();
    static VWPlugInID GetPlugInID();
};

#endif // HELLOWORLD_H
```

**Explications :**
- On hérite de `VWPlugInObject` (classe de base pour les PIO)
- On déclare les méthodes virtuelles `Init` et `Recalculate`
- On définit des méthodes statiques pour l'identification du plugin

---

#### Fichier `HelloWorld.cpp`

```cpp
#include "HelloWorld.h"
#include <VS_Debug.h>

// Identification unique du plugin (GUID)
// Utilisez un GUID unique pour chaque plugin !
const TXString HelloWorld::kPlugInID = "{A1B2C3D4-E5F6-7890-1234-567890ABCDEF}";

// Constructeur
HelloWorld::HelloWorld() {
    VS_OutputDebugString("HelloWorld: Constructeur appelé\n");
}

// Destructeur
HelloWorld::~HelloWorld() {
    VS_OutputDebugString("HelloWorld: Destructeur appelé\n");
}

// Initialisation du plugin
VWErrorCode HelloWorld::Init() {
    VS_OutputDebugString("HelloWorld: Init appelée\n");
    
    // Enregistrer l'objet
    VWErrorCode err = VS_RegisterObject(
        GetPlugInName(),
        GetPlugInDisplayName(),
        kVWObjectTypeCustom,
        this
    );
    
    if (err != kVWNoError) {
        VS_OutputDebugString("Erreur lors de l'enregistrement de l'objet\n");
    }
    
    return err;
}

// Recalcul de la géométrie
VWErrorCode HelloWorld::Recalculate() {
    VS_OutputDebugString("HelloWorld: Recalculate appelée\n");
    
    // Ajouter un texte simple
    VWText text;
    text.SetText("Hello, Vectorworks!");
    text.SetPosition(VWPoint2D(0, 0));
    text.SetFontSize(12);
    AddText(text);
    
    return kVWNoError;
}

// Nom interne du plugin
const char* HelloWorld::GetPlugInName() {
    return "HelloWorld";
}

// Nom affiché dans Vectorworks
const char* HelloWorld::GetPlugInDisplayName() {
    return "Hello World";
}

// ID du plugin
VWPlugInID HelloWorld::GetPlugInID() {
    return kPlugInID;
}

// Fonction d'entrée du plugin (requise par Vectorworks)
extern "C" VWPlugInObject* VWPlugInCreate() {
    return new HelloWorld();
}
```

**Explications :**
- **`kPlugInID`** : Un GUID unique pour identifier votre plugin. **Générez-en un nouveau pour chaque plugin !**
- **`Init()`** : Appelée quand le plugin est chargé. C'est ici qu'on enregistre l'objet.
- **`Recalculate()`** : Appelée quand l'objet doit être redessiné (paramètres changés, etc.).
- **`VWPlugInCreate()`** : Fonction d'entrée **obligatoire** que Vectorworks appelle pour créer une instance de votre plugin.

---

### 4️⃣ Compiler le plugin

#### Avec CMake :

```bash
cd build
cmake --build . --config Release
```

#### Avec Visual Studio :
1. Sélectionnez la configuration **Release**
2. Compilez le projet (F7 ou `Build > Build Solution`)

#### Avec Xcode :
1. Sélectionnez le schéma **Release**
2. Compilez le projet (⌘B ou `Product > Build`)

Le fichier compilé sera :
- **Windows** : `HelloWorld.vso` (dans le dossier `Release`)
- **macOS** : `HelloWorld.vso` (dans le dossier `Products`)

> ⚠️ **Important** : Le fichier doit avoir l'extension `.vso` (pas `.dll` ou `.so`) pour être reconnu par Vectorworks.

---

### 5️⃣ Déployer le plugin

#### Windows :

1. Copiez le fichier `HelloWorld.vso` dans :
   ```
   C:\Program Files\Vectorworks <version>\Plug-ins\
   ```
2. Redémarrez Vectorworks

#### macOS :

1. Ouvrez le Finder
2. Allez dans `/Applications/`
3. Faites un clic droit sur **Vectorworks <version>** > **Afficher le contenu du paquet**
4. Naviguez vers `Contents/Plug-ins/`
5. Copiez votre fichier `HelloWorld.vso`
6. Redémarrez Vectorworks

---

### 6️⃣ Tester le plugin

1. Lancez Vectorworks
2. Ouvrez un nouveau document
3. Dans le menu **Outils > Plugins**, vous devriez voir **Hello World**
4. Sélectionnez l'outil **Hello World**
5. Cliquez dans votre document pour placer l'objet
6. L'objet devrait afficher le texte "Hello, Vectorworks!"

> 🎉 **Félicitations !** Votre premier plugin Vectorworks fonctionne !

---

## 🔍 Dépannage

### Le plugin n'apparaît pas dans Vectorworks

- ✅ Vérifiez que le fichier `.vso` est dans le bon dossier
- ✅ Assurez-vous que le fichier a bien l'extension `.vso`
- ✅ Vérifiez que vous avez redémarré Vectorworks
- ✅ Consultez les logs dans `C:\Users\<user>\AppData\Roaming\Vectorworks\<version>\Logs\`

### Erreur de compilation

- ✅ Vérifiez que les chemins du SDK sont correctement configurés
- ✅ Assurez-vous d'utiliser la bonne version du SDK
- ✅ Vérifiez que vous liez la bonne bibliothèque (`VS_<version>.lib`)

### Vectorworks plante au chargement

- ✅ Vérifiez que votre plugin est compilé en **x64**
- ✅ Assurez-vous d'utiliser le **runtime MD**
- ✅ Simplifiez votre code jusqu'à ce que le problème disparaisse

---

## 🎯 Prochaines étapes

Maintenant que vous avez un plugin fonctionnel, vous pouvez :

1. **[Ajouter des paramètres](https://github.com/69dUbdUb69/Vector_TELESCOPE/tree/main/examples/ParametricBox)** pour créer un objet paramétrique
2. **[Créer une commande personnalisée](https://github.com/69dUbdUb69/Vector_TELESCOPE/tree/main/examples/CustomCommand)**
3. **[Explorer l'API Vectorworks](https://developer.vectorworks.net/api)** pour découvrir plus de fonctionnalités
4. **[Créer un objet 3D](https://developer.vectorworks.net/api/class_v_w_extrude.html)**

---

## 📚 Documentation utile

- [API Reference - VWPlugInObject](https://developer.vectorworks.net/api/class_v_w_plug_in_object.html)
- [API Reference - VS_RegisterObject](https://developer.vectorworks.net/api/group___v_w___registration.html)
- [Guide de développement Vectorworks](https://developer.vectorworks.net/guides)

---

## 📜 Licence

Ce code est sous licence **MIT**. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

*Dernière mise à jour : Août 2024*
*Compatibilité : Vectorworks 2021+*
