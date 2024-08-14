from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Model Training"

class PrepareModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == "__main__":
    try:
        logger.info(f"********************")
        logger.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = PrepareModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e