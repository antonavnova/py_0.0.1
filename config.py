"""
Product: BaseProject
Description: Configuration module for the application
Module: config
Version: 0.0
Build: 1
Created: 2024-10-06
Modified: 2024-10-06
Author: Anton AV Nova (team Stitch In Da House)
License: MIT
Status: Development
"""

import os
from dotenv import load_dotenv

__version__ = "0.0.1"
__author__ = "Anton AV Nova (team Stitch In Da House)"
__license__ = "MIT"
__status__ = "Development"
__all__ = ["Config", "DevelopmentConfig", "ProductionConfig"]

load_dotenv()


class Config:
    """Base configuration"""
    VERSION = __version__
    AUTHOR = __author__
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False