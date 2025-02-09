import sys
import requests

for module_name, modul_path in sys.modules.items():
    print(module_name, modul_path)