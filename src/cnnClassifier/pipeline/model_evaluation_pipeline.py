from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation import ModelEvaluation
from src.cnnClassifier import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def initiate_model_evaluation(self):
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.log_into_mlflow()