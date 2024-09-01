import logging
import os

from from_root import from_root
from datetime import datetime


LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # name of the log how it will appear

log_dir= 'logs' #creating a directory for the log

logs_path=os.path.join(from_root(), log_dir, LOG_FILE) #Creating a pathe 
os.makedirs(log_dir, exist_ok=True) # make the directory

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)