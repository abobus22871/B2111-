import math
import requests
import sys
import inspect

for module_name, modul_path in sys.modules.items():
    print(module_name, modul_path)

print(math.ismodule(requests))
print(math.isclass(requests))
print(math.isfunction(requests))
