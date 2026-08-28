# CMakeLists.txt pour le plugin ParametricBox
# Configuration similaire à HelloWorld mais pour un objet paramétrique

cmake_minimum_required(VERSION 3.20)

# Nom du projet
project(ParametricBox)

# Version de Vectorworks cible
set(VW_VERSION 2024)

# Chemin du SDK Vectorworks
set(VW_SDK_PATH "$ENV{VW_SDK_PATH}")

# Chemin par défaut si VW_SDK_PATH n'est pas défini
if(NOT VW_SDK_PATH)
    if(WIN32)
        set(VW_SDK_PATH "C:/Vectorworks/SDK/${VW_VERSION}")
    elseif(APPLE)
        set(VW_SDK_PATH "/Applications/Vectorworks ${VW_VERSION}/SDK")
    endif()
endif()

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

# Création de la bibliothèque
add_library(${PROJECT_NAME} SHARED ${SOURCES})

# Configuration spécifique à la plateforme
if(WIN32)
    set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".vso")
    target_link_libraries(${PROJECT_NAME} VS_${VW_VERSION}.lib)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        MSVC_RUNTIME_LIBRARY "MultiThreadedDLL"
    )
    set_target_properties(${PROJECT_NAME} PROPERTIES
        WIN32_EXECUTABLE FALSE
    )
elseif(APPLE)
    set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".vso")
    target_link_libraries(${PROJECT_NAME} VS_${VW_VERSION}.dylib)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        MACOSX_RPATH ON
        INSTALL_RPATH "@loader_path"
    )
endif()

# Définitions du préprocesseur
add_define_macros(VW_VERSION=${VW_VERSION})

# Options de compilation
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    add_compile_options(-g)
    add_define_macros(_DEBUG)
else()
    add_compile_options(-O2)
    add_define_macros(NDEBUG)
endif()

message(STATUS "Configuration de ${PROJECT_NAME} terminée avec succès !")
message(STATUS "Fichier de sortie : ${CMAKE_BINARY_DIR}/${CMAKE_BUILD_TYPE}/${PROJECT_NAME}.vso")
