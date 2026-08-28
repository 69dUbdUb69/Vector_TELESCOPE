#ifndef HELLOWORLD_H
#define HELLOWORLD_H

#include <VS_PlugIn.h>

// Classe principale du plugin HelloWorld
// Hérite de VWPlugInObject pour créer un Plug-in Object (PIO)
class HelloWorld : public VWPlugInObject {
public:
    // Constructeur et destructeur
    HelloWorld();
    virtual ~HelloWorld();
    
    // Méthodes virtuelles à implémenter
    // Appelée quand le plugin est initialisé
    virtual VWErrorCode Init() override;
    
    // Appelée quand l'objet doit être recalculé (redessiné)
    virtual VWErrorCode Recalculate() override;
    
    // Méthodes statiques pour l'identification du plugin
    static const char* GetPlugInName();
    static const char* GetPlugInDisplayName();
    static VWPlugInID GetPlugInID();
    
private:
    // ID unique du plugin (GUID)
    // ⚠️ IMPORTANT : Générez un NOUVEAU GUID pour chaque plugin !
    // Utilisez un générateur de GUID en ligne ou Visual Studio (Tools > Create GUID)
    static const TXString kPlugInID;
};

#endif // HELLOWORLD_H
