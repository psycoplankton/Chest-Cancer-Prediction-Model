from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage03_model_training import PrepareModelTrainingPipeline
from cnnClassifier.pipeline.stage04_model_evaluation import PrepareModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"********************")
    logger.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"

try:
    logger.info(f"********************")
    logger.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    obj = PrepareModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"********************")
    logger.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    obj = PrepareModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e