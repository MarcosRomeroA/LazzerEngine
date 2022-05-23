#!/usr/bin/env python

# cli build

# cli run

# cli gen

#cli version

import sys
import subprocess

TOOLS_DIR = "tools"

def RunCommand(cmd):
    subprocess.call("py {}/{}.py".format(TOOLS_DIR, cmd))

for i in range(1, len(sys.argv)):
    cmd = sys.argv[i]

    print("\n-----------------------------\n")
    print("Executing: ", cmd)
    RunCommand(cmd)
    print("\n-----------------------------")