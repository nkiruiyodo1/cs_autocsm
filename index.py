from zoho_connector import *
from config import *
import logging


# Logger settings 
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

auto = SDKInitializer()
auto.update_records()
  
def handler(event, context):  
    try:        
        auto = SDKInitializer()
        auto.update_records()
  

    except Exception as e:
        LOGGER.error(f"The following error occured {e}")