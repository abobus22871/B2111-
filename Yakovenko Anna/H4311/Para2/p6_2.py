import os

path_test = os.path.normpath("C:\\Windows\\Web")

print(os.path.isabs(path_test))
print(os.path.isdir(path_test))
print(os.path.isfile(path_test))
print(os.path.islink(path_test))
