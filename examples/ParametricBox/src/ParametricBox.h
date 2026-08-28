#ifndef PARAMETRICBOX_H
#define PARAMETRICBOX_H

#include <VS_PlugIn.h>

// Classe principale du plugin ParametricBox
// Crée une boîte 3D paramétrique avec des dimensions modifiables
class ParametricBox : public VWPlugInObject {
public:
    // Constructeur et destructeur
    ParametricBox();
    virtual ~ParametricBox();
    
    // Méthodes virtuelles à implémenter
    virtual VWErrorCode Init() override;
    virtual VWErrorCode Recalculate() override;
    
    // Méthodes statiques pour l'identification
    static const char* GetPlugInName();
    static const char* GetPlugInDisplayName();
    static VWPlugInID GetPlugInID();
    
private:
    // ID unique du plugin (GUID)
    // ⚠️ IMPORTANT : Générez un NOUVEAU GUID pour chaque plugin !
    static const TXString kPlugInID;
    
    // Index des paramètres pour un accès plus facile
    // Utiliser un enum permet d'éviter les "magic numbers"
    enum ParamIndex {
        kParamWidth = 0,   // Largeur de la boîte
        kParamHeight,      // Hauteur de la boîte
        kParamDepth,       // Profondeur de la boîte
        kParamColor        // Couleur de la boîte
    };
};

#endif // PARAMETRICBOX_H
