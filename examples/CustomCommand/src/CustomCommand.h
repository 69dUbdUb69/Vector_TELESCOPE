#ifndef CUSTOMCOMMAND_H
#define CUSTOMCOMMAND_H

#include <VS_PlugIn.h>

// Classe principale du plugin CustomCommand
// Hérite de VWPlugInCommand pour créer une commande personnalisée
class CustomCommand : public VWPlugInCommand {
public:
    // Constructeur et destructeur
    CustomCommand();
    virtual ~CustomCommand();
    
    // Méthodes virtuelles à implémenter
    virtual VWErrorCode Init() override;
    
    // Appelée quand la commande est exécutée
    virtual VWErrorCode Execute() override;
    
    // Appelée pour déterminer si la commande est activée
    virtual bool IsEnabled() override;
    
    // Méthodes statiques pour l'identification
    static const char* GetPlugInName();
    static const char* GetPlugInDisplayName();
    static VWPlugInID GetPlugInID();
    
private:
    // ID unique du plugin (GUID)
    // ⚠️ IMPORTANT : Générez un NOUVEAU GUID pour chaque plugin !
    static const TXString kPlugInID;
};

#endif // CUSTOMCOMMAND_H
