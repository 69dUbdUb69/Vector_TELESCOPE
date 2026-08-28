# ⚠️ Problèmes Connus et Solutions

Ce document recense les problèmes courants rencontrés lors du développement de plugins Vectorworks, ainsi que leurs solutions.

---

## 🐛 Problèmes de Compilation

### 1. **Erreur : "Cannot open source file 'VS_*.h'"**
**Cause :** Les chemins d'inclusion du SDK ne sont pas correctement configurés.

**Solution :**
- Vérifiez que la variable d'environnement `VW_SDK_PATH` est définie
- Dans Visual Studio/Xcode, ajoutez le chemin `Include` du SDK aux **Header Search Paths**
- Exemple pour Visual Studio :
  ```
  C:\Vectorworks\SDK\2024\Include
  ```

---

### 2. **Erreur : "LNK1120: unresolved externals"**
**Cause :** Les bibliothèques du SDK ne sont pas correctement liées.

**Solution :**
- Vérifiez que le chemin des bibliothèques (`Lib` ou `Lib\Win64`) est dans les **Library Directories**
- Ajoutez la bibliothèque appropriée (`VS_2024.lib` pour Vectorworks 2024) aux **Additional Dependencies**
- Assurez-vous d'utiliser la bonne architecture (x64)

---

### 3. **Erreur : "DLL load failed"**
**Cause :** Problème de dépendances ou d'architecture.

**Solution :**
- Vérifiez que votre plugin est compilé en **x64** (Vectorworks est uniquement 64 bits)
- Assurez-vous d'utiliser le **runtime MD (Multithreaded DLL)** dans les propriétés du projet
- Vérifiez que toutes les dépendances (DLL externes) sont disponibles
- Utilisez **Dependency Walker** (Windows) pour analyser les dépendances

---

### 4. **Erreur : "The application was unable to start correctly (0xc000007b)"**
**Cause :** Conflit entre architectures 32 bits et 64 bits.

**Solution :**
- Assurez-vous que **toutes** les bibliothèques utilisées sont en 64 bits
- Vérifiez que votre projet est configuré pour **x64** et non **Win32**
- Recompilez toutes vos dépendances en 64 bits

---

## 🔌 Problèmes d'Intégration

### 5. **Plugin non détecté par Vectorworks**
**Cause :** Le fichier `.vso` n'est pas dans le bon dossier ou a des permissions incorrectes.

**Solution :**
- **Windows :** Copiez le `.vso` dans `C:\Program Files\Vectorworks <version>\Plug-ins\`
- **macOS :** Copiez le `.vso` dans `/Applications/Vectorworks <version>/Plug-ins/`
- Vérifiez les permissions du fichier (doit être lisible par tous)
- Redémarrez Vectorworks
- Vérifiez que le fichier a bien l'extension `.vso` (pas `.dll` ou `.so`)

---

### 6. **Plugin détecté mais ne s'affiche pas dans le menu**
**Cause :** Problème dans la fonction `Init` ou `Register` du plugin.

**Solution :**
- Vérifiez que la fonction `Init` retourne `kVWNoError`
- Assurez-vous que `VS_RegisterObject` ou `VS_RegisterCommand` est appelée correctement
- Vérifiez les logs avec `VS_OutputDebugString`
- Exemple de registration correcte :
  ```cpp
  VWErrorCode MyPlugin::Init() {
      VWErrorCode err = VS_RegisterObject(
          "MonPlugin",
          "Mon Plugin",
          kVWObjectTypeCustom,
          this
      );
      if (err != kVWNoError) {
          VS_OutputDebugString("Erreur d'enregistrement de l'objet");
      }
      return err;
  }
  ```

---

### 7. **Vectorworks plante au chargement du plugin**
**Cause :** Exception non gérée dans le constructeur ou `Init`.

**Solution :**
- Entourez le code de `Init` d'un bloc try-catch
- Utilisez `VS_OutputDebugString` pour identifier où le plantage se produit
- Simplifiez votre code jusqu'à ce que le problème disparaisse
- Vérifiez que vous n'accédez pas à des pointeurs nuls

---

### 8. **Plugin fonctionne en debug mais pas en release**
**Cause :** Différences de configuration entre les builds Debug et Release.

**Solution :**
- Vérifiez que les **Runtime Library** sont cohérentes (`/MD` pour les deux)
- Assurez-vous que les **Optimizations** ne causent pas de problèmes
- Vérifiez que les **Preprocessor Definitions** sont identiques
- Testez avec les symboles de débogage activés en Release

---

## 🎨 Problèmes de Plug-in Objects (PIO)

### 9. **Les paramètres ne s'affichent pas dans l'OIP**
**Cause :** Les paramètres ne sont pas correctement enregistrés.

**Solution :**
- Vérifiez que `AddParam` est appelée dans la fonction `Init`
- Assurez-vous que le type de paramètre est correct (`kVWParamTypeReal`, `kVWParamTypeString`, etc.)
- Vérifiez que les options sont correctes (`kVWParamOptReadWrite`)
- Exemple :
  ```cpp
  AddParam("Largeur", kVWParamTypeReal, kVWParamOptReadWrite, 1.0);
  ```

---

### 10. **La géométrie ne s'affiche pas**
**Cause :** Problème dans la fonction `Recalculate` ou `Draw`.

**Solution :**
- Vérifiez que `Recalculate` retourne `kVWNoError`
- Assurez-vous que les objets géométriques sont correctement ajoutés
- Vérifiez que vous utilisez les bonnes coordonnées (2D vs 3D)
- Exemple de dessin 2D :
  ```cpp
  VWErrorCode MyPlugin::Recalculate() {
      VWLine2D line(VWPoint2D(0, 0), VWPoint2D(10, 10));
      AddLine(line);  // Ajoute une ligne au modèle
      return kVWNoError;
  }
  ```

---

### 11. **L'objet ne se met pas à jour quand les paramètres changent**
**Cause :** La fonction `Recalculate` n'est pas appelée ou ne gère pas correctement les paramètres.

**Solution :**
- Vérifiez que vous appelez bien `Recalculate` après un changement de paramètre
- Utilisez `GetParam` pour récupérer les nouvelles valeurs
- Assurez-vous que la géométrie est recalculée avec les nouvelles valeurs
- Exemple :
  ```cpp
  VWErrorCode MyPlugin::Recalculate() {
      double largeur;
      GetParamReal("Largeur", largeur);  // Récupère la valeur actuelle
      
      // Recalcule la géométrie avec la nouvelle valeur
      VWLine2D line(VWPoint2D(0, 0), VWPoint2D(largeur, 0));
      AddLine(line);
      
      return kVWNoError;
  }
  ```

---

### 12. **Les événements souris ne fonctionnent pas**
**Cause :** Les méthodes d'événements ne sont pas correctement surchargées.

**Solution :**
- Assurez-vous que les méthodes sont déclarées avec la bonne signature
- Vérifiez que la classe dérive correctement de la classe de base
- Exemple :
  ```cpp
  class MyPlugin : public VWPlugInObject {
  public:
      virtual VWErrorCode OnMouseDown(VWPoint2D& pt, VWMouseButton button) override;
      // ...
  };
  
  VWErrorCode MyPlugin::OnMouseDown(VWPoint2D& pt, VWMouseButton button) {
      if (button == kVWMouseButtonLeft) {
          VS_OutputDebugString("Clic gauche détecté");
      }
      return kVWNoError;
  }
  ```

---

## 🔧 Problèmes de Commandes Personnalisées

### 13. **La commande ne s'affiche pas dans le menu**
**Cause :** Problème dans l'enregistrement de la commande.

**Solution :**
- Vérifiez que `VS_RegisterCommand` est appelée dans `Init`
- Assurez-vous que la catégorie est correcte (`kVWCommandCategoryCustom`)
- Vérifiez que le nom de la commande est unique
- Exemple :
  ```cpp
  VWErrorCode MyCommand::Init() {
      return VS_RegisterCommand(
          "MaCommande",
          "Exécuter Ma Commande",
          kVWCommandCategoryCustom,
          this
      );
  }
  ```

---

### 14. **La commande est grisée (désactivée)**
**Cause :** La méthode `IsEnabled` retourne `false`.

**Solution :**
- Implémentez la méthode `IsEnabled` pour retourner `true` quand la commande doit être active
- Exemple :
  ```cpp
  bool MyCommand::IsEnabled() {
      // Activer la commande s'il y a des objets sélectionnés
      VWObjectIterator iter(kVWSelectionSetActive);
      return iter.HasNext();
  }
  ```

---

## 🐍 Problèmes avec Python

### 15. **Module 'vs' introuvable**
**Cause :** Python n'est pas correctement configuré dans Vectorworks.

**Solution :**
- Activez Python dans les préférences : `Outils > Préférences > VectorScript/Python`
- Assurez-vous que **Enable Python Scripting** est coché
- Vérifiez que le chemin de Python est correct
- Redémarrez Vectorworks

---

### 16. **Erreur d'importation dans les scripts Python**
**Cause :** La bibliothèque Python n'est pas disponible dans l'environnement de Vectorworks.

**Solution :**
- Utilisez uniquement les bibliothèques standard ou celles fournies avec Vectorworks
- Pour ajouter des bibliothèques tierces :
  1. Trouvez le dossier Python de Vectorworks (ex: `C:\Program Files\Vectorworks <version>\Python`)
  2. Installez la bibliothèque avec `pip install <package> --target <chemin_vers_dossier_python>`
  3. Redémarrez Vectorworks

---

### 17. **Les scripts Python sont lents**
**Cause :** Python est interprétée et donc plus lente que le C++.

**Solution :**
- Optimisez votre code Python (évitez les boucles inutiles)
- Pour les opérations intensives, envisagez de réécrire en C++
- Utilisez des bibliothèques optimisées comme `numpy` pour les calculs
- Exemple d'optimisation :
  ```python
  # Mauvaise pratique : boucle lente
  for i in range(10000):
      vs.Line(i, 0, i, 10)
  
  # Bonne pratique : utiliser des opérations vectorisées
  import numpy as np
  points = np.array([(i, 0, i, 10) for i in range(10000)])
  for pt in points:
      vs.Line(*pt)
  ```

---

## 🔄 Problèmes de Compatibilité

### 18. **Plugin fonctionne sur Windows mais pas sur macOS**
**Cause :** Différences de plateforme non gérées.

**Solution :**
- Utilisez des `#ifdef` pour gérer les différences :
  ```cpp
  #ifdef _WIN32
      // Code Windows
      #include <windows.h>
  #elif defined(__APPLE__)
      // Code macOS
      #include <TargetConditionals.h>
  #endif
  ```
- Vérifiez les chemins des bibliothèques (`.dll` vs `.dylib`)
- Assurez-vous que le code est **endian-safe** (utilisez des types fixes comme `int32_t`)

---

### 19. **Plugin fonctionne sur Vectorworks 2023 mais pas sur 2024**
**Cause :** Changements dans l'API entre les versions.

**Solution :**
- Consultez les **notes de mise à jour** du SDK pour Vectorworks 2024
- Adaptez votre code aux changements de l'API
- Utilisez des `#ifdef` pour gérer les différences :
  ```cpp
  #if VW_VERSION >= 2024
      // Code pour Vectorworks 2024+
  #else
      // Code pour les versions antérieures
  #endif
  ```
- Testez sur les deux versions

---

### 20. **Problèmes avec les versions bêta de Vectorworks**
**Cause :** Les versions bêta peuvent avoir des API instables.

**Solution :**
- Attendez la version finale pour publier votre plugin
- Si vous devez tester sur une bêta :
  - Utilisez le SDK bêta correspondant
  - Signalez les bugs à Vectorworks
  - Ne publiez pas de plugins pour des versions bêta

---

## 📁 Problèmes de Déploiement

### 21. **Les utilisateurs ne voient pas mon plugin**
**Cause :** Problème d'installation ou de permissions.

**Solution :**
- Fournissez des **instructions d'installation claires**
- Créez un **installateur** pour automatiser le processus
- Vérifiez que les utilisateurs ont les **permissions administratives** (Windows)
- Pour macOS, rappelez aux utilisateurs de faire **glisser-déposer** dans le dossier Plug-ins

---

### 22. **Problèmes de signature de code (macOS)**
**Cause :** macOS peut bloquer les plugins non signés.

**Solution :**
- **Signer votre plugin** avec un certificat Apple Developer
- Utilisez la commande :
  ```bash
  codesign --force --sign "Developer ID Application: Votre Nom" MonPlugin.vso
  ```
- Si vous n'avez pas de certificat, les utilisateurs devront **autoriser manuellement** le plugin dans :
  `Préférences Système > Sécurité et Confidentialité > Général`

---

### 23. **Conflits avec d'autres plugins**
**Cause :** Deux plugins utilisent les mêmes noms ou ressources.

**Solution :**
- Utilisez des **noms uniques** pour vos objets, commandes et variables globales
- Évitez les **noms génériques** comme "Utils" ou "Helper"
- Préférez des **namespaces** dans votre code
- Exemple :
  ```cpp
  // ❌ À éviter
  class Helper { ... };
  
  // ✅ Recommandé
  class MonPlugin_Helper { ... };
  ```

---

## 💡 Problèmes Divers

### 24. **Problèmes de mémoire (fuites, corruption)**
**Cause :** Mauvaise gestion de la mémoire.

**Solution :**
- Utilisez les **smart pointers** (`std::unique_ptr`, `std::shared_ptr`)
- Évitez les `new`/`delete` manuels
- Utilisez les **fonctions du SDK** pour la gestion de la mémoire
- Activez les **outils de détection de fuites** (Valgrind, AddressSanitizer)

---

### 25. **Problèmes de performances**
**Cause :** Algorithmes inefficaces ou appels API coûteux.

**Solution :**
- Évitez de recalculer la géométrie inutilement
- Utilisez des **caches** pour les calculs coûteux
- Minimisez les appels à l'API Vectorworks
- Profilez votre code avec des outils comme **Visual Studio Profiler** ou **Instruments** (macOS)

---

### 26. **Problèmes avec les fichiers de ressources**
**Cause :** Les ressources (icônes, images) ne sont pas trouvées.

**Solution :**
- Placez vos ressources dans le **dossier du plugin**
- Utilisez des **chemins relatifs** ou le chemin du plugin :
  ```cpp
  VWString pluginPath;
  VS_GetPluginFolderPath(pluginPath);
  VWString iconPath = pluginPath + "\\ressources\\mon_icone.png";
  ```
- Assurez-vous que les fichiers de ressources sont **inclus dans l'installation**

---

### 27. **Problèmes de localisation (traduction)**
**Cause :** Le plugin n'est pas localisé pour la langue de l'utilisateur.

**Solution :**
- Utilisez les **fonctions de localisation** du SDK :
  ```cpp
  VWString localizedName;
  VS_GetLocalizedString("NomDuPlugin", localizedName);
  ```
- Fournissez des **fichiers de ressources localisés**
- Utilisez des **IDs de chaîne** plutôt que du texte en dur

---

## 🔍 Outils de Diagnostic

### Outils recommandés pour le dépannage :

| Outil | Plateforme | Utilisation |
|-------|-----------|-------------|
| **Visual Studio Debugger** | Windows | Débogage interactif |
| **Xcode Debugger** | macOS | Débogage interactif |
| **Dependency Walker** | Windows | Analyser les dépendances DLL |
| **Process Monitor** | Windows | Surveiller l'activité des fichiers/registre |
| **Console.app** | macOS | Voir les logs système |
| **VS_OutputDebugString** | Tous | Logs de débogage |
| **Vectorworks Logs** | Tous | Logs spécifiques à Vectorworks |

### Où trouver les logs Vectorworks :

**Windows :**
```
C:\Users\<utilisateur>\AppData\Roaming\Vectorworks\<version>\Logs\
```

**macOS :**
```
/Users/<utilisateur>/Library/Logs/Vectorworks/<version>/
```

---

## 📞 Que faire si le problème persiste ?

1. **Consultez** la [documentation officielle](https://developer.vectorworks.net)
2. **Recherchez** sur le [forum développeurs](https://developer.vectorworks.net/forum)
3. **Posez une question** sur le forum avec :
   - La version de Vectorworks
   - La version du SDK
   - Le code source pertinent
   - Le message d'erreur exact
   - Les étapes pour reproduire le problème
4. **Ouvrez un ticket** auprès du support Vectorworks : developer@vectorworks.net
5. **Ouvrez une issue** sur ce dépôt GitHub

---

## 🔄 Mises à jour de ce document

Ce document sera mis à jour régulièrement avec de nouveaux problèmes et solutions. Si vous rencontrez un problème non listé ici, n'hésitez pas à :

- **Ouvrir une issue** sur ce dépôt
- **Proposer une pull request** pour ajouter votre problème et sa solution

---

*Dernière mise à jour : Août 2024*
*Version de Vectorworks supportée : 2021+*
