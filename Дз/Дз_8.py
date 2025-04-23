import logging
logging.basicConfig(level=logging.INFO, filename="logs.log", 
                    filemode="w", format="%(asctime)s - %(message)s")   

a = str(input())
logging.info(a)