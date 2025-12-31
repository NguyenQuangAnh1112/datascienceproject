from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.cnnClassifier.pipeline.data_validation_pipeline import DataValidationPipeline
from src.cnnClassifier.pipeline.data_transformation_pipeline import DataTransformationPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e