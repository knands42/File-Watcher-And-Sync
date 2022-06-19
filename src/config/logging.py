import logging


class LoggingHandler:
    def __init__(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s')
