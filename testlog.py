import logging

LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "D:\Academic\Cloud Computing\log\\logfile.log",
                                level = logging.DEBUG)
logger = logging.getLogger()

#Test the logger
logger.debug("This is a harmless debug message")
logger.info("Just some useful info")
logger.warning("this is warning")
logger.error("This is error")
logger.critical("This is critical")

