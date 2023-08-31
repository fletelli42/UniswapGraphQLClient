# config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Application Settings
APP_NAME = "UniswapGraphQLClient"
APP_VERSION = "1.0.0"
DEBUG = bool(os.getenv('DEBUG', False))

# API Settings
API_ENDPOINT = os.getenv('API_ENDPOINT', 'https://api.example.com/')
API_KEY = os.getenv('API_KEY', 'your_default_api_key')

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'application.log')

# Uniswap Graph Endpoint
UNISWAP_ENDPOINT = os.getenv('UNISWAP_ENDPOINT', 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2')

