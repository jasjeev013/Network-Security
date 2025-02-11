from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=="__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        
        logging.info("Exporting collection as dataframe")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        
        logging.info("Exporting data into feature store")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Validating number of columns")
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
    except NetworkSecurityException as e:
        logging.error(f"Error in main {e}")
    except Exception as e:
        logging.error(f"Error in main {e}")