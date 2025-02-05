## attempt_module_import
Simple module import system that handles errors by asking to install the missing modules via pip

In order to import simply have try_to_import.py as a sibling file with the main one and use: 
```py
import try_to_import
```
Or this if you want to use importlib:
```py
from importlib import import_module
import_module("try_to_import")
```

To import a module using it simply do this:
```py
from try_to_import import *
module = attempt_import("module")

global = attempt_from_import("module","hello_world") # to get a global
global()
```
