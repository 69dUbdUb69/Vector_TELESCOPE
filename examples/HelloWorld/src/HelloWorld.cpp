#include "HelloWorld.h"
#include <VS_Debug.h>
#include <VS_Text.h>

// Identification unique du plugin (GUID)
// ⚠️ IMPORTANT : Générez un NOUVEAU GUID pour chaque plugin !
// Ce GUID est un exemple - utilisez un générateur pour créer le vôtre
const TXString HelloWorld::kPlugInID = "{A1B2C3D4-E5F6-7890-1234-567890ABCDEF}";

// -----------------------------------------------------------------------------
// Constructeur
// Appelé quand une nouvelle instance de l'objet est créée
// -----------------------------------------------------------------------------
HelloWorld::HelloWorld() {
    // Log de débogage (visible dans OutputDebugString ou les logs)
    VS_OutputDebugString("HelloWorld: Constructeur appelé\n");
}

// -----------------------------------------------------------------------------
// Destructeur
// Appelé quand l'objet est détruit
// -----------------------------------------------------------------------------
HelloWorld::~HelloWorld() {
    VS_OutputDebugString("HelloWorld: Destructeur appelé\n");
}

// -----------------------------------------------------------------------------
// Init
// Appelée quand le plugin est chargé par Vectorworks
// C'est ici qu'on enregistre l'objet
// -----------------------------------------------------------------------------
VWErrorCode HelloWorld::Init() {
    VS_OutputDebugString("HelloWorld: Init appelée\n");
    
    // Enregistrer l'objet auprès de Vectorworks
    // Paramètres :
    // 1. Nom interne (utilisé en interne par Vectorworks)
    // 2. Nom affiché (visible dans l'interface)
    // 3. Type d'objet (kVWObjectTypeCustom pour un PIO personnalisé)
    // 4. Pointeur vers l'instance de l'objet
    VWErrorCode err = VS_RegisterObject(
        GetPlugInName(),
        GetPlugInDisplayName(),
        kVWObjectTypeCustom,
        this
    );
    
    if (err != kVWNoError) {
        VS_OutputDebugString("Erreur lors de l'enregistrement de l'objet HelloWorld\n");
    } else {
        VS_OutputDebugString("HelloWorld: Objet enregistré avec succès\n");
    }
    
    return err;
}

// -----------------------------------------------------------------------------
// Recalculate
// Appelée quand l'objet doit être recalculé (redessiné)
// C'est ici qu'on définit la géométrie de l'objet
// -----------------------------------------------------------------------------
VWErrorCode HelloWorld::Recalculate() {
    VS_OutputDebugString("HelloWorld: Recalculate appelée\n");
    
    // Effacer toute géométrie existante
    ClearObjects();
    
    // Créer un objet texte
    VWText text;
    
    // Définir le texte à afficher
    text.SetText("Hello, Vectorworks!");
    
    // Définir la position (coordonnées 2D en mm)
    text.SetPosition(VWPoint2D(0, 0));
    
    // Définir la taille de la police
    text.SetFontSize(12);
    
    // Définir la couleur (optionnel)
    text.SetTextColor(VWColor(255, 0, 0)); // Rouge
    
    // Ajouter le texte au modèle
    AddText(text);
    
    return kVWNoError;
}

// -----------------------------------------------------------------------------
// GetPlugInName
// Retourne le nom interne du plugin (utilisé par Vectorworks)
// -----------------------------------------------------------------------------
const char* HelloWorld::GetPlugInName() {
    return "HelloWorld";
}

// -----------------------------------------------------------------------------
// GetPlugInDisplayName
// Retourne le nom affiché dans l'interface Vectorworks
// -----------------------------------------------------------------------------
const char* HelloWorld::GetPlugInDisplayName() {
    return "Hello World";
}

// -----------------------------------------------------------------------------
// GetPlugInID
// Retourne l'ID unique du plugin
// -----------------------------------------------------------------------------
VWPlugInID HelloWorld::GetPlugInID() {
    return kPlugInID;
}

// -----------------------------------------------------------------------------
// VWPlugInCreate
// Fonction d'entrée OBLIGATOIRE que Vectorworks appelle pour créer
// une nouvelle instance du plugin
// 
// ⚠️ IMPORTANT : Cette fonction DOIT être déclarée comme extern "C"
// et DOIT avoir exactement cette signature
// -----------------------------------------------------------------------------
extern "C" VWPlugInObject* VWPlugInCreate() {
    VS_OutputDebugString("HelloWorld: VWPlugInCreate appelée\n");
    return new HelloWorld();
}
