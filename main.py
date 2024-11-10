from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig

import sys

if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        #print(dataIngestionConfig)
        data = DataIngestion(dataIngestionConfig)

        logging.info("Initated Data Ingestion")
        dataIngestionArtifact = data.initiate_data_ingestion()
        #print(dataIngestionArtifact)
        logging.info("Data Ingestion Completed")
        logging.info("=============*********************==============")

        data_validation_config=DataValidationConfig(trainingPipelineConfig)
        data_validation=DataValidation(dataIngestionArtifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        logging.info("=============*********************==============")

        logging.info("data Transformation started")
        data_transformation_config=DataTransformationConfig(trainingPipelineConfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
        logging.info("=============*********************==============")

    except Exception as e:
        raise NetworkSecurityException(e,sys)