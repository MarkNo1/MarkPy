## FILES & FOLDERS
import os, shutil

# Read File
read = lambda file: open(file, 'r').read()
r=read

# Write File
write = lambda file, text: open(file, 'w').write(text)
w=write

# Append File
append = lambda file, text: open(file, 'a').write(text)
a=append

# Check Existance
exists = lambda file : os.path.exists(file)
e=exists

# Is File
isFile = lambda x : os.path.isfile(x)
isf=isFile

# Is Dir
isDir = lambda x : os.path.isdir(x)
isd=isDir

# Create File
mkfile = lambda file : write(file, '') if not exists(file) else None
mf=mkfile

# Create Folder
mkdir = lambda folder : os.makedirs(folder, exist_ok=True)
md=mkdir

# Remove Folder
rmd = lambda folder : shutil.rmtree(folder)

# Remove File
rmf = lambda file : os.remove(file)

# General Remove
rm = lambda fd : rmf(fd) if isFile(fd) else rmd(fd)

# Joint Path
path = lambda *args : os.path.join(*list(args))
p=path

# List folder
list_folder = lambda path : os.listdir(path)
lsd=list_folder

# File Descriptor
file_descriptor = lambda file : open(file, 'r')
fd=file_descriptor

# Current path
current_path = lambda : os.getcwd()
pwd = current_path

# Basename
basename = lambda path : os.path.basename(path)

# Dir from file
parent_dir = lambda file : '/'.join(file.split('/')[:-1])

# File extension
exts = lambda file : file.split('.')[1] if '.' in file else None

# HD status
disk_usage = shutil.disk_usage

# Get module path
module_path = lambda module : parent_dir(module.__file__)

# Dimensions
b = 1
by = 8 * b
Kby = 1024 * by
Mby = 1024 * Kby
Gby = 1024 * Mby
Tby = 1024 * Gby
Eby = 1024 * Tby
