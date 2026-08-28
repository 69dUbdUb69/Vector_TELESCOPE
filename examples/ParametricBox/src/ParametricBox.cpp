#include "ParametricBox.h"
#include <VS_Debug.h>
#include <VS_Polygon.h>
#include <VS_Extrude.h>

// Identification unique du plugin (GUID)
// ⚠️ IMPORTANT : Générez un NOUVEAU GUID pour chaque plugin !
// Utilisez un générateur de GUID en ligne ou Visual Studio (Tools > Create GUID)
const TXString ParametricBox::kPlugInID = "{B2C3D4E5-F6A7-8901-2345-6789ABCDEF01}";

// -----------------------------------------------------------------------------
// Constructeur
// -----------------------------------------------------------------------------
ParametricBox::ParametricBox() {
    VS_OutputDebugString("ParametricBox: Constructeur appelé\n");
}

// -----------------------------------------------------------------------------
// Destructeur
// -----------------------------------------------------------------------------
ParametricBox::~ParametricBox() {
    VS_OutputDebugString("ParametricBox: Destructeur appelé\n");
}

// -----------------------------------------------------------------------------
// Init
// Initialisation du plugin et enregistrement des paramètres
// -----------------------------------------------------------------------------
VWErrorCode ParametricBox::Init() {
    VS_OutputDebugString("ParametricBox: Init appelée\n");
    
    // Enregistrer l'objet auprès de Vectorworks
    VWErrorCode err = VS_RegisterObject(
        GetPlugInName(),
        GetPlugInDisplayName(),
        kVWObjectTypeCustom,
        this
    );
    
    if (err != kVWNoError) {
        VS_OutputDebugString("Erreur lors de l'enregistrement de l'objet ParametricBox\n");
        return err;
    }
    
    // ========================================================================
    // AJOUT DES PARAMÈTRES
    // ========================================================================
    
    // Largeur de la boîte (en mm)
    // kVWParamTypeReal = nombre décimal
    // kVWParamOptReadWrite = modifiable par l'utilisateur
    // 100.0 = valeur par défaut
    AddParam("Largeur", kVWParamTypeReal, kVWParamOptReadWrite, 100.0);
    
    // Hauteur de la boîte
    AddParam("Hauteur", kVWParamTypeReal, kVWParamOptReadWrite, 100.0);
    
    // Profondeur de la boîte
    AddParam("Profondeur", kVWParamTypeReal, kVWParamOptReadWrite, 100.0);
    
    // Couleur de la boîte
    // kVWParamTypeColor = paramètre de type couleur
    // VWColor(255, 0, 0) = rouge (R, V, B)
    AddParam("Couleur", kVWParamTypeColor, kVWParamOptReadWrite, VWColor(255, 0, 0));
    
    VS_OutputDebugString("ParametricBox: Paramètres enregistrés\n");
    
    return kVWNoError;
}

// -----------------------------------------------------------------------------
// Recalculate
// Recalcule et dessine la géométrie de la boîte en fonction des paramètres
// -----------------------------------------------------------------------------
VWErrorCode ParametricBox::Recalculate() {
    VS_OutputDebugString("ParametricBox: Recalculate appelée\n");
    
    // Effacer toute géométrie existante
    ClearObjects();
    
    // ========================================================================
    // RÉCUPÉRATION DES VALEURS DES PARAMÈTRES
    // ========================================================================
    
    double largeur, hauteur, profondeur;
    VWColor couleur;
    
    // Récupérer les valeurs des paramètres
    // Utilisation de l'enum pour éviter les "magic numbers"
    GetParamReal(kParamWidth, largeur);
    GetParamReal(kParamHeight, hauteur);
    GetParamReal(kParamDepth, profondeur);
    GetParamColor(kParamColor, couleur);
    
    VS_OutputDebugString(TXString::Format("Largeur: %f, Hauteur: %f, Profondeur: %f\n", 
                                          largeur, hauteur, profondeur));
    
    // ========================================================================
    // CRÉATION DE LA GÉOMÉTRIE 2D (BASE DE LA BOÎTE)
    // ========================================================================
    
    // Créer un rectangle centré sur l'origine (0,0)
    // Le rectangle va de -largeur/2 à +largeur/2 en X
    // et de -profondeur/2 à +profondeur/2 en Y
    VWRect2D rect(
        -largeur / 2, -profondeur / 2,  // Coin inférieur gauche
        largeur / 2, profondeur / 2     // Coin supérieur droit
    );
    
    // Créer un polygone à partir du rectangle
    VWPolygon2D polygon;
    polygon.AddVertex(rect.GetMinX(), rect.GetMinY());  // Coin inférieur gauche
    polygon.AddVertex(rect.GetMaxX(), rect.GetMinY());  // Coin inférieur droit
    polygon.AddVertex(rect.GetMaxX(), rect.GetMaxY());  // Coin supérieur droit
    polygon.AddVertex(rect.GetMinX(), rect.GetMaxY());  // Coin supérieur gauche
    polygon.SetClosed(true);  // Fermer le polygone
    
    // ========================================================================
    // EXTRUSION DU POLYGONE POUR CRÉER UNE BOÎTE 3D
    // ========================================================================
    
    // Créer un objet d'extrusion
    VWExtrude extrude;
    
    // Définir le polygone de base
    extrude.SetBasePolygon(polygon);
    
    // Définir le vecteur d'extrusion (hauteur en Z)
    // VWPoint3D(x, y, z) - ici on extrude uniquement en Z
    extrude.SetExtrusionVector(VWPoint3D(0, 0, hauteur));
    
    // Type d'extrusion : verticale (perpendiculaire au plan XY)
    extrude.SetExtrusionType(kVWExtrusionTypeVertical);
    
    // Définir les couleurs
    extrude.SetPenColor(couleur);    // Couleur du contour
    extrude.SetFillColor(couleur);   // Couleur de remplissage
    
    // Ajouter l'extrusion au modèle
    AddExtrude(extrude);
    
    VS_OutputDebugString("ParametricBox: Géométrie créée avec succès\n");
    
    return kVWNoError;
}

// -----------------------------------------------------------------------------
// GetPlugInName
// -----------------------------------------------------------------------------
const char* ParametricBox::GetPlugInName() {
    return "ParametricBox";
}

// -----------------------------------------------------------------------------
// GetPlugInDisplayName
// -----------------------------------------------------------------------------
const char* ParametricBox::GetPlugInDisplayName() {
    return "Parametric Box";
}

// -----------------------------------------------------------------------------
// GetPlugInID
// -----------------------------------------------------------------------------
VWPlugInID ParametricBox::GetPlugInID() {
    return kPlugInID;
}

// -----------------------------------------------------------------------------
// VWPlugInCreate
// Fonction d'entrée OBLIGATOIRE
// -----------------------------------------------------------------------------
extern "C" VWPlugInObject* VWPlugInCreate() {
    VS_OutputDebugString("ParametricBox: VWPlugInCreate appelée\n");
    return new ParametricBox();
}
