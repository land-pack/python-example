from project.utils.log import logger
from project.model.models import get_expire_redpacket, rollback

def hello():
    logger.debug("hello")
 

def rollback_unspent_redpacket():
    d = get_expire_redpacket()
    for i in d:
        logger.warning("Try to rollback expire order: %s", i)
        rollback(i)
