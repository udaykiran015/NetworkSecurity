from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        data_ingestion=DataIngestion(data_ingestion_config=DataIngestionConfig(TrainingPipelineConfig()))
        logging.info("Initiated the data ingestion component")
        dataingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(dataingestion_artifact)
        logging.info("Data ingestion completed successfully")
        
    except Exception as e:
        # We catch the ZeroDivisionError and wrap it in our custom exception
        logging.error("Dividing by zero is not allowed.")
        raise NetworkSecurityException(e, sys)