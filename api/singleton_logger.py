import logging

class LoggerSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            cls._instance.logger = logging.getLogger("IRISapi")
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls._instance.logger.addHandler(handler)
            cls._instance.logger.setLevel(logging.INFO)
        return cls._instance
    