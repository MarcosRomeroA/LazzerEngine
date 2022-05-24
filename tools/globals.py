V_MAJOR = 1
V_MINOR = 0

import sys, platform

PLATFORM = sys.platform

for x in platform.uname():
    if "microsoft" in x.lower():
        PLATFORM = "windows"
        break

def IsWindows():
    return PLATFORM == "windows"

def isLinux():
    return PLATFORM == "linux"

def isMac():
    return PLATFORM == "darwin"