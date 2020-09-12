## FILES & FOLDERS
import os, shutil

# Read File
read = lambda file: open(file, 'r').read()
r=read

# Write File
write = lambda file, text: open(file, 'w').write(text)

# Append File
append = lambda file, text: open(file, 'a').write(text)

# Check Existance
exists = lambda file : os.path.exists(file)

# Is File
isFile = lambda x : os.path.isfile(x)

# Is Dir
isDir = lambda x : os.path.isdir(x)

# Create empty File
mkfile = lambda file : write(file, '') if not exists(file) else None

# Create File with x  as content
New = lambda file, x : write(file, x)

# Create Folder
mkdir = lambda folder : os.makedirs(folder, exist_ok=True)

# Remove Folder
rmd = lambda folder : shutil.rmtree(folder)

# Remove File
rmf = lambda file : os.remove(file)

# General Remove
rm = lambda fd : rmf(fd) if isFile(fd) else rmd(fd)

# Joint Path
path = lambda *args : os.path.join(*list(args))

# List folder
list_folder = lambda path : os.listdir(path)

# File Descriptor
file_descriptor = lambda file : open(file, 'r')

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
bit = 1
byte = 8 * bit
Kbyte = 1024 * byte
Mbyte = 1024 * Kbyte
Gbyte = 1024 * Mbyte
Tbyte = 1024 * Gbyte
Ebyte = 1024 * Tbyte
