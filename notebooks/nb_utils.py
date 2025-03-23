import sys
from pathlib import Path

def set_root(level: int=1):
    if level != 0:
        for i in range(level):
            if i == 0:
                PROJECT_DIR = Path.cwd().parent
            else:
                PROJECT_DIR = PROJECT_DIR.parent
    else:
        PROJECT_DIR = Path.cwd()
    sys.path.append(str(PROJECT_DIR))
    return PROJECT_DIR
    

def create_dir(*args):
    """
    Creates directories from a mix of Path objects and string paths. 
    If a directory already exists, it does nothing for that directory.
    """
    for arg in args:
        path = Path(arg)  # Ensure arg is a Path object
        path.mkdir(parents=True, exist_ok=True)