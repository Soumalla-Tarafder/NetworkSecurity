from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig


import sys

if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        print(dataIngestionConfig)
        data = DataIngestion(dataIngestionConfig)

        logging.info("Initated Data Ingestion")
        dataIngestionArtifdact = data.initiate_data_ingestion()
        print(dataIngestionArtifdact)
        logging.info("Data Ingestion Completed")

    except Exception as e:
        raise NetworkSecurityException(e,sys)