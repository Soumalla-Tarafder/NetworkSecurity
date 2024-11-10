from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig


import sys

if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        print(dataIngestionConfig)
        data = DataIngestion(dataIngestionConfig)

        logging.info("Initated Data Ingestion")
        dataIngestionArtifact = data.initiate_data_ingestion()
        print(dataIngestionArtifact)
        logging.info("Data Ingestion Completed")

        data_validation_config=DataValidationConfig(trainingPipelineConfig)
        data_validation=DataValidation(dataIngestionArtifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")


    except Exception as e:
        raise NetworkSecurityException(e,sys)