from dataclasses import dataclass

@dataclass

class DataIngestionArtifact:
    """Data Ingestion Artifact"""
    train_file_path:str
    test_file_path:str
    