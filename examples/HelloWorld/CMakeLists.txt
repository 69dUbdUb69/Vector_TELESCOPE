# CMakeLists.txt pour le plugin HelloWorld
# Ce fichier configure la compilation du plugin Vectorworks

cmake_minimum_required(VERSION 3.20)

# Nom du projet
project(HelloWorld)

# Version de Vectorworks cible
# Modifiez cette valeur selon votre version du SDK
set(VW_VERSION 2024)

# Chemin du SDK Vectorworks
# Peut être défini via la variable d'environnement VW_SDK_PATH
set(VW_SDK_PATH "$ENV{VW_SDK_PATH}")

# Si VW_SDK_PATH n'est pas défini, utiliser un chemin par défaut
if(NOT VW_SDK_PATH)
    # Chemin par défaut pour Windows
    if(WIN32)
        set(VW_SDK_PATH "C:/Vectorworks/SDK/${VW_VERSION}")
    # Chemin par défaut pour macOS
    elseif(APPLE)
        set(VW_SDK_PATH "/Applications/Vectorworks ${VW_VERSION}/SDK")
    endif()
endif()

# Afficher le chemin du SDK (pour le débogage)
message(STATUS "VW_SDK_PATH: ${VW_SDK_PATH}")

# Vérifier que le SDK existe
if(NOT EXISTS ${VW_SDK_PATH}/Include)
    message(FATAL_ERROR "SDK Vectorworks non trouvé à : ${VW_SDK_PATH}")
endif()

# Configuration du projet
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Dossiers d'inclusion
include_directories(
    ${VW_SDK_PATH}/Include
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

# Dossiers des bibliothèques
link_directories(${VW_SDK_PATH}/Lib)

# Fichiers sources
file(GLOB SOURCES "src/*.cpp")

# Création de la bibliothèque (DLL / Dynamic Library)
add_library(${PROJECT_NAME} SHARED ${SOURCES})

# Configuration spécifique à la plateforme
if(WIN32)
    # Windows : utiliser l'extension .vso
    set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".vso")
    
    # Bibliothèques à lier
    target_link_libraries(${PROJECT_NAME} VS_${VW_VERSION}.lib)
    
    # Configuration du runtime (Multithreaded DLL)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        MSVC_RUNTIME_LIBRARY "MultiThreadedDLL"
    )
    
    # Architecture (x64)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        WIN32_EXECUTABLE FALSE
    )
    
elseif(APPLE)
    # macOS : utiliser l'extension .vso
    set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".vso")
    
    # Bibliothèques à lier
    target_link_libraries(${PROJECT_NAME} VS_${VW_VERSION}.dylib)
    
    # Configuration spécifique macOS
    set_target_properties(${PROJECT_NAME} PROPERTIES
        MACOSX_RPATH ON
        INSTALL_RPATH "@loader_path"
    )
    
endif()

# Définitions du préprocesseur
add_define_macros(VW_VERSION=${VW_VERSION})

# Options de compilation (Debug vs Release)
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    # Options de débogage
    add_compile_options(-g)
    add_define_macros(_DEBUG)
else()
    # Options de release
    add_compile_options(-O2)
    add_define_macros(NDEBUG)
endif()

# Dossier de sortie
# Par défaut, CMake place les fichiers dans le dossier build
# Vous pouvez personnaliser cela si nécessaire

# Afficher un message de succès
message(STATUS "Configuration de ${PROJECT_NAME} terminée avec succès !")
message(STATUS "Fichier de sortie : ${CMAKE_BINARY_DIR}/${CMAKE_BUILD_TYPE}/${PROJECT_NAME}.vso")
