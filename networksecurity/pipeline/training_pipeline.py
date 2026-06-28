import os
import sys
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)
from networksecurity.entity.artifact_entity import(
   DataIngestionArtifact,
   DataValidationArifact,
   DataTransfomrationArifact,
   ModelTrainerArtifact
)

class TrainingPipeline:
    def __init__(self):
       self.training_pipeline_config= TrainingPipelineConfig()
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
          self.data_ingestion_config=DataIngestionConfig(self.training_pipeline_config)
          logging.info("Initiated the data ingestion component")
          data_ingestion=DataIngestion(self.data_ingestion_config)
          data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
          logging.info(f"Data ingestion completed successfully {data_ingestion_artifact}")
          return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArifact:
       try:
          self.data_validation_config=DataValidationConfig(self.training_pipeline_config)
          logging.info("Data Validation intitaited")
          data_validation=DataValidation(data_ingestion_artifact,self.data_validation_config)
          data_validation_artifact=data_validation.initiate_data_validation()
          logging.info("Data Validation completed")
          return data_validation_artifact
       except Exception as e:
          raise NetworkSecurityException(e,sys)
    def start_data_transformation(self,data_validation_artifact:DataValidationArifact)->DataTransfomrationArifact:
       try:
          self.data_transformation_config=DataTransformationConfig(self.training_pipeline_config)
          logging.info("Data Transdformation  intitaited")
          data_transformation=DataTransformation(data_validation_artifact,self.data_transformation_config)
          data_transformation_artifact=data_transformation.initiate_data_transformation()
          logging.info("Data Transdformation  completed")
          return data_transformation_artifact
       except Exception as e:
          raise NetworkSecurityException(e,sys)
    def start_model_trainer(self,data_transformation_artifact:DataTransfomrationArifact)->ModelTrainerArtifact:
       try:
          self.model_trainer_config=ModelTrainerConfig(self.training_pipeline_config)
          logging.info("Model Trainer starting")
          model_trainer=ModelTrainer(self.model_trainer_config,data_transformation_artifact)
          model_trainer_artifact=model_trainer.initiate_model_trainer()
          logging.info("Model Trainer Finished")
          return model_trainer_artifact
       except Exception as e:
          raise NetworkSecurityException(e,sys)
    def run_pipeline(self):
       try:
          data_ingestion_artifact=self.start_data_ingestion()
          data_validation_artifact=self.start_data_validation(data_ingestion_artifact)
          data_transformation_artifact=self.start_data_transformation(data_validation_artifact)
          model_trainer_artifact=self.start_model_trainer(data_transformation_artifact)
          return model_trainer_artifact
       except Exception as e:
          raise NetworkSecurityException(e,sys)

        