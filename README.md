## attempt_module_import
Simple module import system that handles errors by asking to install the missing modules via pip

In order to import simply have attempt_module_import as a sibling file with the main one and use: 
```py
import attempt_module_import
```
Or this if you want to use importlib:
```py
from importlib import import_module
import_module("attempt_module_import")
```
