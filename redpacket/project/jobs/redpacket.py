from project.utils.log import logger
from project.model.models import get_expire_redpacket

def hello():
    logger.debug("hello")
 

def rollback_unspent_redpacket():
    d = get_expire_redpacket()
    print(d)
