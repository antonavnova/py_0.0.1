"""
Product: BaseProject
Description: Basic Python project structure for GitHub deployment
Module: main
Version: 0.0
Build: 1
Created: 2024-10-06
Modified: 2024-10-06
Author: Anton AV Nova (team Stitch In Da House)
License: MIT
Status: Development
"""

__version__ = "0.0.1"
__author__ = "Anton AV Nova (team Stitch In Da House)"
__license__ = "MIT"
__status__ = "Development"
# Добавляем __version__ в __all__ чтобы её можно было импортировать
__all__ = ["main", "__version__", "__author__", "__license__", "__status__"]

def main():
    """Основная функция приложения"""
    print("🚀 Project started successfully!")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    return True

if __name__ == "__main__":
    main()