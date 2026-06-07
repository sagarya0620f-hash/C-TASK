import os
import platform
import sys

print("Operating System:", platform.system())
print("Username:", os.getlogin())
print("Current Directory:", os.getcwd())
print("Python Version:", sys.version)