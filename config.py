# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration constants
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEB3_INFURA_URL = os.getenv('WEB3_INFURA_URL')
WEB3_BSC_URL = os.getenv('WEB3_BSC_URL')
WEB3_BASE_URL = os.getenv('WEB3_BASE_URL')
SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL')
ETH_PRIVATE_KEY = os.getenv('ETH_PRIVATE_KEY')
BSC_PRIVATE_KEY = os.getenv('BSC_PRIVATE_KEY')
SOL_PRIVATE_KEY = os.getenv('SOL_PRIVATE_KEY')
BASE_PRIVATE_KEY = os.getenv('BASE_PRIVATE_KEY')

# Print out the variables for debugging
print(f'TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN}')
print(f'WEB3_INFURA_URL: {WEB3_INFURA_URL}')
print(f'WEB3_BSC_URL: {WEB3_BSC_URL}')
print(f'WEB3_BASE_URL: {WEB3_BASE_URL}')
print(f'SOLANA_RPC_URL: {SOLANA_RPC_URL}')
print(f'ETH_PRIVATE_KEY: {ETH_PRIVATE_KEY}')
print(f'BSC_PRIVATE_KEY: {BSC_PRIVATE_KEY}')
print(f'SOL_PRIVATE_KEY: {SOL_PRIVATE_KEY}')
print(f'BASE_PRIVATE_KEY: {BASE_PRIVATE_KEY}')
