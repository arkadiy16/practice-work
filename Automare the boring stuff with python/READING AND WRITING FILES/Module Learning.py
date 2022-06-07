import os
from pathlib import Path


# Introduction with Path() function
sub_folder = Path('spam', 'bacon', 'eggs')

print(sub_folder)
print(type(sub_folder))
str_sub_folder = str(sub_folder)
print(str_sub_folder)
print(type(str_sub_folder))


# Introduction with / operator to join paths
pth1 = Path('bacon', 'direct', 'folder1')
pth2 = Path('eggs', 'learning')
pth3 = Path('eggs/learning')
s_pth = 'eggs/learning'

print(pth1 / pth2) # Next 3 examples are equel
print(pth1 / pth3)
print(pth1 / s_pth)

print(s_pth / s_pth) # Errors because at least first or second of joining paths should be Path object
print(s_pth / s_pth / pth1)


# Introdaction with Path.cwd() and os.chdir()
a = Path.cwd()
print(a) # C:\Users\1\Desktop

os.chdir('C:\\Users\\Docs\\NewFolder')
 
d = Path.cwd()
print(d) # C:\Users\Docs\NewFolder
