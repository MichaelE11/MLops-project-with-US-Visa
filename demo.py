from US_Visa.logger import logging
import sys
from US_Visa.exception import USvisaException

logging.info("welcome to our custom loggingh")

try:
    2/0
except Exception as e:
    raise USvisaException(e,sys) from e