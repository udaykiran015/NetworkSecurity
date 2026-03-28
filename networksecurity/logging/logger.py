import logging
import os
from datetime import datetime

# 1. Define the directory where logs will live
LOGS_DIR = os.path.join(os.getcwd(), 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

# 2. Define the unique filename using a timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# 3. Create the full path to the file
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# 4. Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

