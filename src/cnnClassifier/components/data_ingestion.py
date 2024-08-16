import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            if os.path.exists(zip_download_dir):
                logger.info(f"File already exists at {zip_download_dir}, skipping download.")
            else:
                logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

                # Extract the file ID from the URL
                file_id = dataset_url.split("/")[-2]
                # Google Drive download URL format
                prefix = 'https://drive.google.com/uc?export=download&id='

                # Download the file using gdown
                gdown.download(prefix + file_id, zip_download_dir, quiet=False)
                
                logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """Extracts zip file into data directory"""
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(unzip_path)
            
            
