import logging
#logging.basicConfig(level=logging.ERROR)
logging.basicConfig(filename="./debugging.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d")
#name = 'joe'
logging.error("this is an error")
logging.critical("critical error")
logging.warning("warning")
logging.info("FYI:")
logging.debug("Debug note:")