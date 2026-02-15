import sys
from pathlib import Path
from colorama import Fore, Style

def get_directory_path():
    # 1. Перевіряємо, чи передано аргумент
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Використання: python directory_tree.py <шлях_до_директорії>")
        print(Style.RESET_ALL)
        return None
    else:
        # 2. Отримуємо шлях
        path = Path(sys.argv[1])
        
        # 3. Перевіряємо, чи існує шлях
        if not path.exists():
            print(Fore.RED + f"Помилка: шлях '{path}' не існує" + Style.RESET_ALL)
            return None
        
        # 4. Перевіряємо, чи це директорія
        if not path.is_dir():
            print(Fore.RED + f"Помилка: '{path}' не є директорією" + Style.RESET_ALL)
            return None
        
        return path
    
def display_tree(directory, indent=0):
    try:
        for item in directory.iterdir():
            prefix = "  " * indent

            if item.is_dir():
                print(Fore.BLUE + prefix + f"📁 [{item.name}]" + Style.RESET_ALL)
                display_tree(item, indent + 1)
            else:
                print(Fore.GREEN + prefix + f"📄 {item.name}" + Style.RESET_ALL)
                
    except PermissionError:
        print(Fore.RED + prefix + "  [Доступ заборонено]" + Style.RESET_ALL)
    

if __name__ == "__main__":
    directory = get_directory_path()

    if directory:
        print(Fore.CYAN + f"\nСтруктура директорії: {directory}\n" + Style.RESET_ALL)
        display_tree(directory)

