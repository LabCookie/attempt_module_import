# This is a custom module that tries to import a module but if failed, the user has to choose to either install with pip or
# exit the program alltogether. It will request you to restart the program after the installation of such module.
dont_ask = False

__all__ = [
    "attempt_import",
    "attempt_from_import",
	"dont_ask"
]

import importlib
from os import name,system
from subprocess import check_call
from sys import executable

def clr():
    # Clears console but detects os before doing so
    # making sure the command exists in the os.
    if name == "nt":
        system("cls")
    else:
        system("clear")
def handle_importerror(module,e):
	if not dont_ask:
	    clr()
	    choice = ""
	    while not choice.upper() in ["Y","N"]: # Perform a loop until the user's choice (but capitalized) is either Y or N
	        choice = input(f"{e} Would you like to install it using pip? \nY/N: ")
	    if choice.upper() == "Y":
	        install_module(module)
	        input("Thank you. Press the enter key to continue")
	    else:
	        exit()
	else:
		install_module(module)
def install_module(module):
    # Calls pip to install a module
    check_call([executable,"-m","pip","install",module])

def attempt_from_import(module,attr):
    try:
        # Returns with the global from module
        return getattr(importlib.import_module(module), attr)
    except ImportError as e:
        handle_importerror(module,e)
def attempt_import(module):
    try:
        # Attempt to import the module while handling the importerror
        return importlib.import_module(module)
    except ImportError as e:
        handle_importerror(module,e)
