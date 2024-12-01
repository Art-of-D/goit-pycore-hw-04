import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def get_directory_tree() -> None:
    if len(sys.argv) < 2:
        print(Fore.RED + "Error: Please provide a directory path as an argument.")
        return
    
    directory = Path(sys.argv[1])

    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + "Error: The provided path does not exist or is not a directory.")
        return

    print(Fore.YELLOW + f"Directory tree for: {directory}\n")

    def traverse_dir(path, level=0):
      indent = " " * (level * 4)
      if path.is_dir():
          print(Fore.BLUE + f"{indent}{path.name}/")
          for item in path.iterdir():
              traverse_dir(item, level + 1)
      else:
          print(Fore.GREEN + f"{indent}{path.name}")
        
    traverse_dir(directory)

if __name__ == "__main__":
    get_directory_tree()