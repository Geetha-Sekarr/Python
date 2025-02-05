import logging
logging.basicConfig(filename="c://unit test.py",filemode='w',)
log=logging.getLogger()
log.debug("this is debug")
log.info("this is info")
log.error("this is error")
log.warning("this is warning log")
log.critical("this is critical log")