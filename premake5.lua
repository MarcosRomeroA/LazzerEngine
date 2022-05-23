workspace "LazzerEngine"
    startproject "LazzerEngineEditor"
    architecture "x64"

    configurations
    {
        "Debug",
        "Release"
    }

project "LazzerEngineEditor"
    location "LazzerEngineEditor"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++17"

    files
    {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp"
    }

    flags
    {
        "FatalWarnings"
    }

