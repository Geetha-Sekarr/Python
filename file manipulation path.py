#creating path object
from pathlib import Path
p = Path('.')
p2 = Path('/home/user/docs')

#path methods
#/opreator
p = Path('/home/user')
p2 = p / 'documents'

#path information
p = Path('/home/user/docs/file.txt')
print(p.name)
print(p.stem)
print(p.suffix)
if p.exists():
    print(f"{p} exists.")
else:
    print(f"{p}does not exists.")
#if p.is_file():
    #print(f"{p}is a file")
#if p.is_dir():
    #print(f"{p}is a directory)


#File system opreations
p = Path('/home/user/new_dir')
p.mkdir(parents=True, exist_ok=True)
p.rmdir()
p.rename()
p.unlink()


#If working with the file urls and web urls using urlparse
from urllib.parse import urlparse
uri = 'file:///home/user/documents/example.txt'
parsed=urlparse(uri)
print(f"File name{parsed.scheme}")
print(f"Path{parsed.path}")

#expanding path
from pathlib import path
p = Path('~/documents/file.txt')
extended=p.expanduser()
print(f"expand path{extended}")

#resolving path
from pathlib import Path
relative_path = Path('documents/example.txt')
absolute_path=relative_path.resolve()
print(absolute_path) 

#both use expanding and resolving path
from pathlib import Path
single_path=Path('documents/example.txt')
both_path=single_path.expanduser().resolve()

#querying file 
from pathlib import Path
file_path = Path('example.txt')
if file_path.is_file():
    print(f"{file_path} is a regular file.")
if file_path.is_dir():
    print(f"{file_path} is a directory.")
if file_path.is_symlink():
    print(f"{file_path} is a symbolic link.")
    



