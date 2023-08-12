import logging

logging.basicConfig(
    filename="LOG.log",
    filemode="a",
    format="%(asctime)s %(name)s %(levelname)s %(message)s ",
)
my_logger = logging.getLogger("Shoaib")
my_logger.critical("The is please Erro")
