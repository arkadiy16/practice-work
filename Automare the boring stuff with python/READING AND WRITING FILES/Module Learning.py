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


# Introdaction with os.makedirs() and Path().mkdir().
os.makedirs('C:\\Users\\Desktop\\New\\Foo\\Bar') # Create new folders: \New\Foo\Bar
Path('C:\\Users\\1\\Desktop\\FBar').mkdir() # Create only 1 folder: \FBar


# Introduction with absolute and relative paths.
print(Path.cwd()) # C:\Users\1\Desktop
print(Path.cwd().is_absolute()) # True
print(Path('foo/bar').is_absolute()) # False
print(os.path.isabs(Path.cwd())) # Same as line before previous but with os module.


relative_path = Path('Foo/Bar') 
print(Path.cwd() / relative_path) # Making absolute path from relative path with / operator and Path.cwd() function
print(os.path.abspath(f'.\\{relative_path}')) # Same as past but with os.path.abspath() function.

print(os.path.abspath('.')) # Absolute path to cwd.
print(os.path.abspath('..')) # Absolute path to parent folder cwd.
print(os.path.abspath('\\')) # Local disk of cwd.

print(os.path.relpath('C:\\Users\\1\\Desktop', '\\Users')) # Turning absolute path to relative.
