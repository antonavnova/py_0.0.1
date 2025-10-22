"""
Product: BaseProject
Description: Tests for main module
Module: test_main
Version: 0.0
Build: 1
Created: 2024-10-06
Modified: 2024-10-06
Author: Anton AV Nova (team Stitch In Da House)
License: MIT
Status: Development
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import main, __version__ as main_version

# Добавляем main_version в __all__ чтобы убрать варнинг
__all__ = ["test_main_function", "test_version", "main_version"]

def test_main_function():
    """Test the main function returns True"""
    assert main() == True

def test_version():
    """Test the version of MAIN module is correct"""
    assert main_version == "0.0.1"  # Используем main_version, а не __version__