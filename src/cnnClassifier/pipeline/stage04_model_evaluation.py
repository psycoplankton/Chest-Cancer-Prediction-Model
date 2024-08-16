from cnnClassifier.components.model_evaluation import Evaluation
from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Model Evaluation"

class PrepareModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f"********************")
        logger.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = PrepareModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e