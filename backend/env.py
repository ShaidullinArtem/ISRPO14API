import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()


class Environment:
    SECRET_KEY: Final = os.environ.get('SECRET_KEY', '')
    DEBUG: Final = os.environ.get('DEBUG', True)
