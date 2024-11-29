import os

def print_structure(startpath, level=0, exclude_dirs=None):
    """
    Рекурсивно выводит структуру каталогов, исключая определенные папки.
    """
    exclude_dirs = exclude_dirs or []
    for item in os.listdir(startpath):
        item_path = os.path.join(startpath, item)
        if os.path.basename(item_path) in exclude_dirs:
            continue  # Пропускаем исключенные папки
        prefix = '├── ' if level > 0 else ''
        print(f"{'│   ' * (level - 1) if level > 1 else ''}{prefix}{item}")
        if os.path.isdir(item_path) and not item.startswith('.'):
            print_structure(item_path, level + 1, exclude_dirs)

if __name__ == "__main__":
    print("Структура проекта:")
    # Укажите папки, которые хотите исключить
    print_structure('.', exclude_dirs=['venv', 'frontend', '__pycache__', '.git'])
