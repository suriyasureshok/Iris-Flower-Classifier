import os
import joblib
from api.singleton_logger import LoggerSingleton

class Model_loader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Model_loader, cls).__new__(cls)
            logger = LoggerSingleton().logger
            try:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                model_path = os.path.join(base_dir, "../model/iris_clf_model.pkl")
                logger.info(f"Loading model from {model_path}")
                cls._instance.model = joblib.load(model_path)
                logger.info("Model loaded successfully.")
            except Exception as e:
                logger.error(f"Model loading failed: {e}")
                raise e
        return cls._instance
