# ❓ FAQ - Questions Fréquentes sur les Plugins Vectorworks

## 📌 Général

### Q: Quel langage utiliser pour développer un plugin Vectorworks ?
**R:** 
- **C++** : Le langage principal et recommandé pour les plugins natifs (performances optimales, accès complet à l'API)
- **Python** : Possible depuis Vectorworks 2021, plus simple mais avec des limitations
- **VectorScript** : Langage historique (basé sur Pascal), utile pour des scripts simples

### Q: Ai-je besoin d'une licence Vectorworks spéciale pour développer des plugins ?
**R:** Non, une licence standard suffit. Cependant, la version **Developer** de Vectorworks inclut des outils supplémentaires pour le débogage.

### Q: Puis-je vendre mes plugins ?
**R:** Oui ! Vectorworks encourage le développement de plugins tiers. Vous pouvez les vendre via :
- Votre propre site web
- Le [Vectorworks Marketplace](https://marketplace.vectorworks.net)
- Des plateformes comme Gumroad, Sellfy, etc.

### Q: Mes plugins fonctionneront-ils sur toutes les versions de Vectorworks ?
**R:** Non, les plugins sont généralement spécifiques à une version majeure de Vectorworks. Vous devrez :
- Compiler séparément pour chaque version
- Adapter votre code aux changements de l'API
- Tester sur chaque version cible

---

## 🛠️ Développement

### Q: Comment installer le SDK Vectorworks ?
**R:** Voir la section [Prérequis](../README.md#-prérequis) dans le README principal.

### Q: Où trouver la documentation de l'API ?
**R:** 
- **Documentation officielle** : [developer.vectorworks.net/api](https://developer.vectorworks.net/api)
- **Headers C++** : Les fichiers `VS_*.h` dans le dossier `Include` du SDK contiennent des commentaires détaillés
- **Exemples** : Le SDK inclut des exemples dans le dossier `Samples`

### Q: Comment déboguer un plugin Vectorworks ?
**R:** 
1. **Attacher le débogueur** :
   - Visual Studio : `Debug > Attach to Process > Vectorworks.exe`
   - Xcode : `Debug > Attach to Process > Vectorworks`
2. **Utiliser des logs** : `VS_OutputDebugString("Mon message de débogage");`
3. **Fichier de log** : Vectorworks écrit des logs dans `C:\Users\<user>\AppData\Roaming\Vectorworks\<version>\Logs\`

### Q: Pourquoi mon plugin ne s'affiche pas dans Vectorworks ?
**R:** Vérifiez :
- ✅ Le fichier `.vso` (Windows) ou `.vso` (macOS) est bien dans le bon dossier :
  - Windows : `C:\Program Files\Vectorworks <version>\Plug-ins\`
  - macOS : `/Applications/Vectorworks <version>/Plug-ins/`
- ✅ Le plugin est compilé pour la bonne architecture (x64)
- ✅ Le plugin est compilé pour la bonne version de Vectorworks
- ✅ Le fichier `.vso` a les bonnes permissions (lecture/écriture)
- ✅ Vectorworks a été redémarré après l'installation

### Q: Comment forcer Vectorworks à recharger mon plugin ?
**R:** 
1. Fermez Vectorworks
2. Supprimez le fichier `.vso` de votre plugin
3. Copiez la nouvelle version
4. Redémarrez Vectorworks

> ⚠️ **Astuce** : Vous pouvez aussi utiliser la commande **Rechargez les Plug-ins** dans le menu **Outils > Plugins** (si disponible dans votre version).

### Q: Pourquoi Vectorworks plante-t-il quand je charge mon plugin ?
**R:** Causes possibles :
- **Exception non gérée** dans votre code C++
- **Mauvaise version de runtime** (utilisez `/MD` pour Multithreaded DLL)
- **Problème de dépendances** (bibliothèques manquantes)
- **Conflit de versions** entre le SDK utilisé et Vectorworks

**Solution :**
1. Vérifiez les logs dans le dossier `Logs` de Vectorworks
2. Utilisez le débogueur pour identifier où le plantage se produit
3. Simplifiez votre code jusqu'à ce que le problème disparaisse

---

## 🎯 Plug-in Objects (PIO)

### Q: Comment créer un objet paramétrique simple ?
**R:** Voir l'exemple [ParametricBox](../examples/ParametricBox/) dans ce dépôt.

### Q: Comment ajouter des paramètres à mon PIO ?
**R:** Utilisez la classe `VWParametric` et la fonction `AddParam` :

```cpp
// Dans la fonction Init de votre plugin
VWErrorCode MyPlugin::Init() {
    // Ajouter un paramètre numérique
    AddParam("Largeur", kVWParamTypeReal, kVWParamOptReadWrite, 1.0);
    
    // Ajouter un paramètre texte
    AddParam("Nom", kVWParamTypeString, kVWParamOptReadWrite, "Mon Objet");
    
    // Ajouter un paramètre booléen
    AddParam("Actif", kVWParamTypeBool, kVWParamOptReadWrite, true);
    
    return kVWNoError;
}
```

### Q: Comment accéder aux valeurs des paramètres ?
**R:**

```cpp
// Récupérer la valeur d'un paramètre numérique
double largeur;
GetParamReal("Largeur", largeur);

// Récupérer la valeur d'un paramètre texte
char nom[256];
GetParamString("Nom", nom, 256);

// Récupérer la valeur d'un paramètre booléen
bool actif;
GetParamBool("Actif", actif);
```

### Q: Comment mettre à jour la géométrie de mon PIO ?
**R:** Implémentez la méthode `Recalculate` :

```cpp
VWErrorCode MyPlugin::Recalculate() {
    // Récupérer les paramètres
    double largeur, hauteur, profondeur;
    GetParamReal("Largeur", largeur);
    GetParamReal("Hauteur", hauteur);
    GetParamReal("Profondeur", profondeur);
    
    // Créer la géométrie
    VWPoint3D pt1(0, 0, 0);
    VWPoint3D pt2(largeur, 0, 0);
    VWPoint3D pt3(largeur, hauteur, 0);
    VWPoint3D pt4(0, hauteur, 0);
    
    // Ajouter un polygone 2D
    VWLine2D line;
    line.Set(pt1, pt2);
    AddLine(line);
    
    // ... ajouter d'autres éléments géométriques ...
    
    return kVWNoError;
}
```

### Q: Comment gérer les événements (clic, survol, etc.) ?
**R:** Surchargez les méthodes virtuelles de la classe de base :

```cpp
// Appelé quand l'utilisateur clique sur l'objet
VWErrorCode MyPlugin::OnMouseDown(VWPoint2D& pt, VWMouseButton button) {
    if (button == kVWMouseButtonLeft) {
        VS_OutputDebugString("Clic gauche sur l'objet");
    }
    return kVWNoError;
}

// Appelé quand la souris passe sur l'objet
VWErrorCode MyPlugin::OnMouseOver(VWPoint2D& pt) {
    // Changer la couleur de survol
    SetPenColor(kVWColorRed);
    return kVWNoError;
}
```

---

## 🔧 Commandes Personnalisées

### Q: Comment créer une commande personnalisée ?
**R:** Voir l'exemple [CustomCommand](../examples/CustomCommand/) dans ce dépôt.

### Q: Comment ajouter ma commande au menu ?
**R:** Utilisez la fonction `VS_RegisterCommand` dans la fonction `Init` de votre plugin :

```cpp
VWErrorCode MyCommandPlugin::Init() {
    // Enregistrer la commande
    VWErrorCode err = VS_RegisterCommand(
        "MaCommande",           // Nom interne
        "Exécuter Ma Commande", // Nom affiché
        kVWCommandCategoryCustom, // Catégorie
        this                    // Pointeur vers l'objet command
    );
    
    if (err != kVWNoError) {
        VS_OutputDebugString("Erreur lors de l'enregistrement de la commande");
    }
    
    return err;
}
```

### Q: Comment exécuter du code quand ma commande est appelée ?
**R:** Implémentez la méthode `Execute` :

```cpp
VWErrorCode MyCommandPlugin::Execute() {
    // Code à exécuter
    VS_OutputDebugString("Ma commande a été exécutée !");
    
    // Exemple : Sélectionner tous les objets
    VWObjectIterator iter(kVWSelectionSetActive);
    VWObjectHandle hObj;
    
    while (iter.Next(hObj)) {
        // Faire quelque chose avec chaque objet sélectionné
    }
    
    return kVWNoError;
}
```

---

## 🐍 Python

### Q: Comment utiliser Python dans Vectorworks ?
**R:** 
1. Activez Python dans les préférences : `Outils > Préférences > VectorScript/Python`
2. Utilisez l'éditeur de scripts : `Outils > Scripts > Éditeur de Scripts`
3. Sélectionnez **Python** comme langage

### Q: Quelles bibliothèques Python sont disponibles ?
**R:** 
- **Bibliothèques standard** : La plupart des bibliothèques de la standard library sont disponibles
- **vs** : Module spécifique à Vectorworks (`import vs`)
- **numpy** : Disponible dans les versions récentes
- **Autres bibliothèques** : Doivent être installées dans l'environnement Python de Vectorworks

### Q: Comment accéder à l'API Vectorworks depuis Python ?
**R:** Utilisez le module `vs` :

```python
import vs

# Créer un point
pt = vs.VWPoint3D(1.0, 2.0, 3.0)

# Dessiner une ligne
vs.Line(0, 0, 10, 10)

# Sélectionner des objets
handles = vs.GetSelectedObjects()
for h in handles:
    print(f"Objet sélectionné : {h}")
```

### Q: Où trouver la documentation du module `vs` ?
**R:** 
- [Python Scripting Guide](https://developer.vectorworks.net/python)
- Utilisez `dir(vs)` et `help(vs.fonction)` dans l'interpréteur Python de Vectorworks

---

## 🔄 VectorScript

### Q: Quelle est la différence entre VectorScript et Python ?
**R:**

| Caractéristique | VectorScript | Python |
|----------------|--------------|--------|
| **Syntaxe** | Basé sur Pascal | Syntaxe moderne |
| **Performances** | Bonnes | Moyennes |
| **Accès à l'API** | Complet | Partiel |
| **Apprentissage** | Courbe abrupte | Plus facile |
| **Bibliothèques** | Limitées | Nombreuses |

### Q: Comment créer une procédure VectorScript ?
**R:**

```pascalscript
PROCEDURE MaProcedure;
VAR
    x, y : REAL;
    h : HANDLE;
BEGIN
    x := 0;
    y := 0;
    
    { Créer un cercle }
    h := Circle(x, y, 5);
    
    { Définir la couleur }
    SetColor(h, 255, 0, 0); { Rouge }
END;
RUN(MaProcedure);
```

### Q: Comment exécuter un script VectorScript ?
**R:** 
1. Ouvrez l'éditeur de scripts : `Outils > Scripts > Éditeur de Scripts`
2. Collez votre code
3. Cliquez sur **Exécuter** ou appuyez sur F5

---

## 🐞 Dépannage

### Q: Mon plugin ne compile pas, que faire ?
**R:** 
1. Vérifiez que les chemins du SDK sont correctement configurés
2. Assurez-vous d'utiliser la bonne version du SDK
3. Vérifiez que vous liez les bonnes bibliothèques (`VS_<version>.lib`)
4. Consultez les erreurs de compilation pour identifier le problème

### Q: Mon plugin compile mais ne fonctionne pas, que faire ?
**R:**
1. Vérifiez que le fichier `.vso` est dans le bon dossier
2. Utilisez `VS_OutputDebugString` pour ajouter des logs
3. Attachez le débogueur pour voir où le code s'arrête
4. Simplifiez votre code jusqu'à ce qu'il fonctionne

### Q: Mon plugin fonctionne sur ma machine mais pas sur celle d'un client, que faire ?
**R:**
1. Vérifiez que le client a la bonne version de Vectorworks
2. Assurez-vous que le plugin est compilé pour la bonne architecture (x64)
3. Vérifiez que toutes les dépendances sont incluses
4. Demandez au client de vérifier les logs dans `C:\Users\<user>\AppData\Roaming\Vectorworks\<version>\Logs\`

### Q: Comment gérer les différences entre Windows et macOS ?
**R:** Utilisez des `#ifdef` pour gérer les différences de plateforme :

```cpp
#ifdef _WIN32
    // Code spécifique à Windows
    #include <windows.h>
#elif defined(__APPLE__)
    // Code spécifique à macOS
    #include <TargetConditionals.h>
#endif
```

---

## 📦 Distribution

### Q: Comment packager mon plugin pour la distribution ?
**R:** 
1. Créez une archive ZIP contenant :
   - Le fichier `.vso` (Windows) ou `.vso` (macOS)
   - Un fichier `README.md` avec les instructions d'installation
   - Un fichier `LICENSE` si applicable
   - Des exemples ou des fichiers de démonstration

2. **Structure recommandée** :
   ```
   MonPlugin-v1.0.0/
   ├── MonPlugin.vso
   ├── README.md
   ├── LICENSE
   ├── examples/
   │   └── demo.vwx
   └── docs/
       └── installation.md
   ```

### Q: Comment installer un plugin manuellement ?
**R:** 

**Windows :**
1. Copiez le fichier `.vso` dans :
   `C:\Program Files\Vectorworks <version>\Plug-ins\`
2. Redémarrez Vectorworks

**macOS :**
1. Ouvrez le Finder
2. Allez dans `/Applications/`
3. Faites un clic droit sur **Vectorworks <version>** > **Afficher le contenu du paquet**
4. Naviguez vers `Contents/Plug-ins/`
5. Copiez votre fichier `.vso`
6. Redémarrez Vectorworks

### Q: Comment désinstaller un plugin ?
**R:** Supprimez simplement le fichier `.vso` du dossier `Plug-ins` et redémarrez Vectorworks.

---

## 🔄 Mises à jour

### Q: Comment gérer les mises à jour de mon plugin ?
**R:** 
1. **Versionnage** : Utilisez un système de versionnage sémantique (ex: `v1.0.0`)
2. **Compatibilité** : Testez chaque mise à jour sur toutes les versions supportées
3. **Changelog** : Maintenez un fichier `CHANGELOG.md` pour documenter les changements
4. **Notifications** : Informez vos utilisateurs des mises à jour via :
   - Votre site web
   - Un système de notification dans le plugin (si possible)
   - Les réseaux sociaux

### Q: Comment gérer les migrations entre versions de Vectorworks ?
**R:**
1. Testez votre plugin sur la nouvelle version bêta du SDK
2. Adaptez votre code aux changements de l'API
3. Publiez une nouvelle version de votre plugin compatible
4. Informez vos utilisateurs des exigences de version

---

## 🚀 Conseils pour les débutants

### Q: Par où commencer si je suis nouveau en développement Vectorworks ?
**R:** 
1. **[Lisez le README principal](../README.md)** de ce dépôt
2. **Installez le SDK** et explorez les exemples fournis
3. **Commencez par VectorScript** pour comprendre les concepts de base
4. **Passez à Python** pour un développement plus rapide
5. **Enfin, apprenez le C++** pour des plugins performants

### Q: Quels sont les meilleurs exemples pour apprendre ?
**R:** 
- **[HelloWorld](../examples/HelloWorld/)** : Plugin minimal en C++
- **[ParametricBox](../examples/ParametricBox/)** : Objet paramétrique simple
- **Exemples du SDK** : Le dossier `Samples` du SDK contient des exemples officiels

### Q: Comment rester à jour avec les nouveautés ?
**R:** 
- **Abonnez-vous** à la newsletter développeur Vectorworks
- **Suivez** le [blog Vectorworks](https://www.vectorworks.net/fr/blog)
- **Participez** au [forum développeurs](https://developer.vectorworks.net/forum)
- **Rejoignez** la communauté sur Discord ou Slack (si disponible)

---

## 📞 Support supplémentaire

Si vous ne trouvez pas de réponse à votre question :

1. **Consultez** la [documentation officielle](https://developer.vectorworks.net)
2. **Posez une question** sur le [forum développeurs](https://developer.vectorworks.net/forum)
3. **Ouvrez une issue** sur ce dépôt GitHub
4. **Contactez** le support Vectorworks : developer@vectorworks.net

---

*Dernière mise à jour : Août 2024*
