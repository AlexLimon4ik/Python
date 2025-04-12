import logging
# r-read w-write перезаписує  a-не перезаписує але робить все
logging.basicConfig(level=logging.DEBUG, filename="logs.log", 
                    filemode="w", format="We have next logging message: %(asctime)s:%(levelname)s - %(message)s")     

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")

assert 2 + 2 == 5, "wrong answer"