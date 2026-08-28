# 🚀 Apprendre à créer un plugin Vectorworks

Ce dépôt est un guide complet pour créer des plugins (modules externes) pour **Vectorworks**, le logiciel de CAO/DAO utilisé en architecture, design et aménagement paysager.

---

## 📚 Sommaire

1. [Introduction aux plugins Vectorworks](#-introduction-aux-plugins-vectorworks)
2. [Prérequis](#-prérequis)
3. [Structure d'un plugin](#-structure-dun-plugin)
4. [Types de plugins](#-types-de-plugins)
5. [Exemples pratiques](#-exemples-pratiques)
6. [Compilation et débogage](#-compilation-et-débogage)
7. [Bonnes pratiques](#-bonnes-pratiques)
8. [Ressources utiles](#-ressources-utiles)

---

## 🎯 Introduction aux plugins Vectorworks

Un **plugin Vectorworks** (ou *plug-in object* / *PIO*) est un module externe qui étend les fonctionnalités du logiciel. Les plugins permettent de :

- ✅ Créer des objets paramétriques personnalisés
- ✅ Ajouter de nouvelles commandes et outils
- ✅ Automatiser des tâches répétitives
- ✅ Intégrer des calculs ou des logiques métiers spécifiques
- ✅ Connecter Vectorworks à d'autres logiciels ou bases de données

> ⚠️ **Important** : Vectorworks utilise principalement le **langage C++** pour le développement de plugins natifs. Il existe aussi des solutions en **Python** via le module `vs` (VectorScript), mais avec des limitations.

---

## 🛠️ Prérequis

### Logiciels nécessaires

| Outil | Version | Lien | Notes |
|-------|---------|------|-------|
| **Vectorworks** | 2023+ | [vectorworks.net](https://www.vectorworks.net) | Version Developer recommandée |
| **Visual Studio** | 2019+ | [visualstudio.microsoft.com](https://visualstudio.microsoft.com) | Pour Windows |
| **Xcode** | 14+ | Mac App Store | Pour macOS |
| **CMake** | 3.20+ | [cmake.org](https://cmake.org) | Optionnel mais recommandé |
| **Git** | - | [git-scm.com](https://git-scm.com) | Pour le versionnage |

### SDK Vectorworks

Le **Software Development Kit (SDK)** de Vectorworks est **indispensable** pour développer des plugins. Il contient :

- Les headers C++ (`VS_*.h`)
- Les bibliothèques (`VS_*.dll` / `.dylib` / `.so`)
- La documentation technique
- Des exemples de code

> 📥 **Comment obtenir le SDK ?**
> - Téléchargeable depuis le [portail développeurs Vectorworks](https://developer.vectorworks.net)
> - Nécessite un compte développeur (gratuit)
> - Disponible pour Windows et macOS

### Installation du SDK

1. Téléchargez le SDK correspondant à votre version de Vectorworks
2. Extrayez-le dans un dossier (ex: `C:\Vectorworks\SDK\2024`)
3. Configurez vos variables d'environnement :
   ```bash
   # Windows (PowerShell)
   $env:VW_SDK_PATH = "C:\Vectorworks\SDK\2024"
   
   # macOS (Terminal)
   export VW_SDK_PATH="/Applications/Vectorworks 2024/SDK"
   ```

---

## 📁 Structure d'un plugin

Voici la structure typique d'un projet de plugin Vectorworks :

```
MonPlugin/
├── src/
│   ├── MonPlugin.cpp          # Code principal du plugin
│   ├── MonPlugin.h            # Déclarations des classes
│   └── ressources/            # Icônes, images, etc.
├── include/
│   └── VS_*.h                 # Headers du SDK (liens symboliques)
├── lib/
│   └── VS_*.lib/.dylib        # Bibliothèques du SDK
├── CMakeLists.txt             # Configuration CMake
├── MonPlugin.vcxproj          # Projet Visual Studio (Windows)
├── MonPlugin.xcodeproj        # Projet Xcode (macOS)
└── README.md
```

---

## 🎨 Types de plugins

Vectorworks supporte plusieurs types de plugins :

### 1. **Plug-in Objects (PIO)** ⭐

Les objets paramétriques personnalisés. C'est le type le plus courant.

**Caractéristiques :**
- S'insèrent comme des objets natifs dans le dessin
- Ont des paramètres éditables via l'OIP (Object Info Palette)
- Peuvent avoir une géométrie 2D et/ou 3D

**Exemple d'utilisation :**
- Un meuble paramétrique (hauteur, largeur, matériau)
- Un escalier personnalisé
- Un élément architectural complexe

### 2. **Commandes personnalisées**

Ajoutent de nouvelles commandes au menu ou à la palette d'outils.

**Caractéristiques :**
- Accessibles via le menu **Outils > Plugins**
- Peuvent être assignées à des raccourcis clavier
- Exécutent une action spécifique

### 3. **Fonctions VectorScript**

Scripts en langage VectorScript (basé sur Pascal) pour automatiser des tâches.

**Limites :**
- Moins performant que le C++
- Accès limité à l'API
- Pas de compilation nécessaire

### 4. **Modules Python**

Depuis Vectorworks 2021, il est possible d'écrire des scripts Python.

**Avantages :**
- Syntaxe plus simple
- Prototypage rapide
- Accès à de nombreuses bibliothèques Python

**Limites :**
- Performances inférieures au C++
- Certaines fonctionnalités de l'API ne sont pas disponibles

---

## 💻 Exemples pratiques

Consultez le dossier [`/examples`](./examples) pour des exemples complets :

- [HelloWorld Plugin](examples/HelloWorld/) - Plugin minimal pour démarrer
- [ParametricBox](examples/ParametricBox/) - Boîte paramétrique 3D
- [CustomCommand](examples/CustomCommand/) - Commande personnalisée
- [VectorScript Example](examples/VectorScript/) - Exemple en VectorScript
- [Python Example](examples/Python/) - Exemple en Python

---

## 🔨 Compilation et débogage

### Configuration de Visual Studio (Windows)

1. Créez un nouveau projet **Dynamic Link Library (DLL)**
2. Ajoutez les chemins du SDK :
   - **Include Directories** : `$VW_SDK_PATH\Include`
   - **Library Directories** : `$VW_SDK_PATH\Lib\Win64`
   - **Libraries** : `VS_2024.lib` (selon la version)
3. Définissez le **Runtime Library** : `/MD` (Multithreaded DLL)
4. Configurez les **Preprocessor Definitions** : `VW_VERSION=2024`

### Configuration de Xcode (macOS)

1. Créez un nouveau projet **Dynamic Library**
2. Ajoutez les chemins du SDK dans **Header Search Paths**
3. Ajoutez les bibliothèques dans **Link Binary With Libraries**
4. Configurez les **Preprocessor Macros** : `VW_VERSION=2024`

### Débogage

**Astuce :** Pour déboguer un plugin Vectorworks :

1. **Attacher le débogueur** à Vectorworks.exe
2. **Utiliser des logs** avec `VS_OutputDebugString()`
3. **Gérer les exceptions** : Vectorworks peut planter si votre plugin génère une exception non gérée

```cpp
// Exemple de log de débogage
#include <VS_Debug.h>

void MonPlugin::DebugLog(const char* message) {
    VS_OutputDebugString(message);
    VS_OutputDebugString("\n");
}
```

### Fichier CMakeLists.txt de base

```cmake
cmake_minimum_required(VERSION 3.20)
project(MonPlugin)

# Configuration de la version
set(VW_VERSION 2024)

# Chemins du SDK
set(VW_SDK_PATH "$ENV{VW_SDK_PATH}")
if(NOT VW_SDK_PATH)
    set(VW_SDK_PATH "/Applications/Vectorworks ${VW_VERSION}/SDK")
endif()

# Inclusions
include_directories(
    ${VW_SDK_PATH}/Include
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# Bibliothèques
link_directories(${VW_SDK_PATH}/Lib)

# Fichiers sources
file(GLOB SOURCES "src/*.cpp")

# Création de la bibliothèque
add_library(${PROJECT_NAME} SHARED ${SOURCES})

# Configuration spécifique à la plateforme
if(WIN32)
    target_link_libraries(${PROJECT_NAME} VS_${VW_VERSION}.lib)
    set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".vso")
elseif(APPLE)
    target_link_libraries(${PROJECT_NAME} VS_${VW_VERSION}.dylib)
    set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".vso")
endif()

# Définitions du préprocesseur
add_define_macros(VW_VERSION=${VW_VERSION})
```

---

## ✅ Bonnes pratiques

### 1. **Gestion de la mémoire**

- ❌ **À éviter** : `new` / `delete` sans gestion propre
- ✅ **À faire** : Utiliser les smart pointers ou les fonctions du SDK

```cpp
// Bon : Utilisation des fonctions du SDK
VWPoint3D* pt = new VWPoint3D(x, y, z);
// ... utilisation ...
delete pt;

// Mieux : Utilisation des classes du SDK
VWPoint3D pt(x, y, z);
```

### 2. **Gestion des erreurs**

Toujours vérifier les codes de retour des fonctions du SDK :

```cpp
VWErrorCode err = VS_GetObject(hObject, &obj);
if (err != kVWNoError) {
    // Gérer l'erreur
    VS_OutputDebugString("Erreur lors de la récupération de l'objet");
    return err;
}
```

### 3. **Compatibilité entre versions**

- Utilisez des `#ifdef` pour gérer les différences entre versions
- Testez sur plusieurs versions de Vectorworks
- Évitez les fonctionnalités spécifiques à une version

```cpp
#ifdef VW_2024
    // Code spécifique à Vectorworks 2024
#elif defined(VW_2023)
    // Code spécifique à Vectorworks 2023
#endif
```

### 4. **Documentation**

- Documentez votre code avec des commentaires **Doxygen**
- Créez un fichier **README.md** pour chaque plugin
- Utilisez des noms de variables et fonctions explicites

### 5. **Tests**

- Testez votre plugin sur différents types de documents
- Vérifiez les cas limites (valeurs nulles, objets supprimés, etc.)
- Utilisez des outils comme **Google Test** pour les tests unitaires

---

## 📖 Ressources utiles

### Documentation officielle

- [Vectorworks Developer Portal](https://developer.vectorworks.net) - Portal principal
- [SDK Documentation](https://developer.vectorworks.net/sdk) - Documentation technique
- [API Reference](https://developer.vectorworks.net/api) - Référence de l'API
- [VectorScript Reference](https://developer.vectorworks.net/vectorscript) - Référence VectorScript

### Communautés et forums

- [Vectorworks Community Board](https://forum.vectorworks.net) - Forum officiel
- [Vectorworks Developer Forum](https://developer.vectorworks.net/forum) - Forum développeurs
- [GitHub Vectorworks](https://github.com/Vectorworks) - Dépôts officiels

### Exemples et tutoriels

- [Vectorworks SDK Samples](https://github.com/Vectorworks/Vectorworks-SDK-Samples) - Exemples officiels
- [VectorScript Cookbook](https://developer.vectorworks.net/vectorscript/cookbook) - Recettes VectorScript
- [Python Scripting Guide](https://developer.vectorworks.net/python) - Guide Python

### Livres et formations

- **Vectorworks Developer Guide** (PDF) - Disponible dans le SDK
- **Mastering Vectorworks** - Livre avec un chapitre sur les plugins
- [Vectorworks University](https://university.vectorworks.net) - Formations en ligne

---

## 🚀 Prochaines étapes

1. **[Installer le SDK Vectorworks](#-prérequis)**
2. **[Créer votre premier plugin](examples/HelloWorld/README.md)** avec l'exemple HelloWorld
3. **[Explorer l'API](https://developer.vectorworks.net/api)** pour découvrir les possibilités
4. **[Rejoindre la communauté](https://developer.vectorworks.net/forum)** pour poser des questions

---

## 📞 Support

Si vous avez des questions ou rencontrez des problèmes :

1. Consultez la **[FAQ](docs/FAQ.md)**
2. Parcourez les **[problèmes connus](docs/KNOWN_ISSUES.md)**
3. Ouvrez une **[issue](https://github.com/69dUbdUb69/Vector_TELESCOPE/issues)** sur ce dépôt
4. Posez une question sur le **[forum développeurs](https://developer.vectorworks.net/forum)**

---

## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre d'utiliser, modifier et distribuer ce code.

```
MIT License

Copyright (c) 2024 Vector_TELESCOPE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

*Dernière mise à jour : Août 2024*
*Compatibilité : Vectorworks 2021+*
