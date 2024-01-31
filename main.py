
from src.custom_logger import logger


from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_validation_pipeline import DataValidationPipeline


if __name__ == '__main__':

    STAGE_NAME = 'DATA_INGESTION'        
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    STAGE_NAME = 'DATA_VALIDATION'        
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")


    
  
