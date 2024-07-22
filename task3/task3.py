import sys
from pathlib import Path
from colorama import Fore, Style, init

init()


directory_path = Path(sys.argv[1])
if not directory_path.exists():
    print("There is no such directory.")
    sys.exit(1)

if not directory_path.is_dir():
    print("It is not a directory.")
    sys.exit(1)


def print_directory_structure(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
            print_directory_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

print_directory_structure(directory_path)