#include "CustomCommand.h"
#include <VS_Debug.h>
#include <VS_Object.h>
#include <VS_Alert.h>

// Identification unique du plugin (GUID)
// ⚠️ IMPORTANT : Générez un NOUVEAU GUID pour chaque plugin !
const TXString CustomCommand::kPlugInID = "{C3D4E5F6-A7B8-9012-3456-789ABCDEF012}";

// -----------------------------------------------------------------------------
// Constructeur
// -----------------------------------------------------------------------------
CustomCommand::CustomCommand() {
    VS_OutputDebugString("CustomCommand: Constructeur appelé\n");
}

// -----------------------------------------------------------------------------
// Destructeur
// -----------------------------------------------------------------------------
CustomCommand::~CustomCommand() {
    VS_OutputDebugString("CustomCommand: Destructeur appelé\n");
}

// -----------------------------------------------------------------------------
// Init
// Initialisation du plugin et enregistrement de la commande
// -----------------------------------------------------------------------------
VWErrorCode CustomCommand::Init() {
    VS_OutputDebugString("CustomCommand: Init appelée\n");
    
    // Enregistrer la commande auprès de Vectorworks
    // Paramètres :
    // 1. Nom interne de la commande
    // 2. Nom affiché dans le menu
    // 3. Catégorie (kVWCommandCategoryCustom = Outils > Plugins > Custom)
    // 4. Pointeur vers l'instance de la commande
    VWErrorCode err = VS_RegisterCommand(
        GetPlugInName(),
        GetPlugInDisplayName(),
        kVWCommandCategoryCustom,
        this
    );
    
    if (err != kVWNoError) {
        VS_OutputDebugString("Erreur lors de l'enregistrement de la commande CustomCommand\n");
    } else {
        VS_OutputDebugString("CustomCommand: Commande enregistrée avec succès\n");
    }
    
    return err;
}

// -----------------------------------------------------------------------------
// Execute
// Exécute la logique de la commande
// Appelée quand l'utilisateur clique sur la commande dans le menu
// -----------------------------------------------------------------------------
VWErrorCode CustomCommand::Execute() {
    VS_OutputDebugString("CustomCommand: Execute appelée\n");
    
    // ========================================================================
    // COMPTER LE NOMBRE D'OBJETS SÉLECTIONNÉS
    // ========================================================================
    
    VWObjectIterator iter(kVWSelectionSetActive);
    VWObjectHandle hObj;
    int count = 0;
    
    // Parcourir tous les objets sélectionnés
    while (iter.Next(hObj)) {
        count++;
    }
    
    // ========================================================================
    // AFFICHER UN MESSAGE AVEC LE NOMBRE D'OBJETS
    // ========================================================================
    
    TXString message;
    if (count == 0) {
        message = "Aucun objet sélectionné !";
    } else if (count == 1) {
        message = "1 objet sélectionné.";
    } else {
        message = TXString::Format("%d objets sélectionnés.", count);
    }
    
    // Afficher une boîte de dialogue
    // kVWAlertOK = bouton OK
    // kVWAlertNote = icône d'information
    VS_Alert(
        TXString("Commande personnalisée\n\n") + message,
        kVWAlertOK,
        kVWAlertNote
    );
    
    // ========================================================================
    // MODIFIER LES OBJETS SÉLECTIONNÉS
    // ========================================================================
    
    if (count > 0) {
        // Réinitialiser l'itérateur pour parcourir à nouveau
        iter.Reset();
        
        // Parcourir à nouveau les objets sélectionnés
        while (iter.Next(hObj)) {
            // Changer la couleur de chaque objet en vert
            VWColor newColor(0, 255, 0); // Vert (R, V, B)
            VS_SetObjectColor(hObj, newColor);
        }
        
        // Mettre à jour l'affichage pour voir les changements
        VS_UpdateDisplay();
        
        VS_OutputDebugString(TXString::Format("CustomCommand: %d objets modifiés\n", count));
    }
    
    return kVWNoError;
}

// -----------------------------------------------------------------------------
// IsEnabled
// Détermine si la commande est activée (non grisée) dans le menu
// -----------------------------------------------------------------------------
bool CustomCommand::IsEnabled() {
    // La commande est activée s'il y a au moins un objet sélectionné
    VWObjectIterator iter(kVWSelectionSetActive);
    bool hasSelection = iter.HasNext();
    
    VS_OutputDebugString(TXString::Format(
        "CustomCommand: IsEnabled appelée - Sélection: %s\n",
        hasSelection ? "Oui" : "Non"
    ));
    
    return hasSelection;
}

// -----------------------------------------------------------------------------
// GetPlugInName
// -----------------------------------------------------------------------------
const char* CustomCommand::GetPlugInName() {
    return "CustomCommand";
}

// -----------------------------------------------------------------------------
// GetPlugInDisplayName
// -----------------------------------------------------------------------------
const char* CustomCommand::GetPlugInDisplayName() {
    return "Custom Command";
}

// -----------------------------------------------------------------------------
// GetPlugInID
// -----------------------------------------------------------------------------
VWPlugInID CustomCommand::GetPlugInID() {
    return kPlugInID;
}

// -----------------------------------------------------------------------------
// VWPlugInCreate
// Fonction d'entrée OBLIGATOIRE
// -----------------------------------------------------------------------------
extern "C" VWPlugInObject* VWPlugInCreate() {
    VS_OutputDebugString("CustomCommand: VWPlugInCreate appelée\n");
    return new CustomCommand();
}
