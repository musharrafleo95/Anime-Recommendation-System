import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
from utils.common_functions import read_yaml


logger = get_logger(__name__)


class DataIngestion:
    def __init__(self, config):
        self.random_seed = config.get('random_seed', 42)
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]

        # creating raw directory
        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info("Data ingestion initialized")

    def download_csv_from_gcp(self):
        try:
            logger.info("Starting getting data from Gcloud")
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_names:
                op_file_path = os.path.join(RAW_DIR, file_name)
                blob = bucket.blob(file_name)

                if file_name == "animelist.csv":
                    self.download_first_n_rows(blob=blob, output_file=op_file_path, num_rows=5000000)
                    logger.info(f"Dowloaded 5M rows for file: {file_name}")
                else:
                    blob.download_to_filename(op_file_path)

                logger.info(f"File: {file_name} downloaded from GCP")

        except Exception as e:
            error_message = "Faced error in downloading csv from GCP"
            logger.info(error_message)
            raise CustomException(error_message, e)

    def download_first_n_rows(self, blob, output_file, num_rows=50):
        """Downloads the first N rows of a CSV file from GCS."""
        try:
            logger.info("Streaming csv from gcp") 
            with open(output_file, 'w') as f_out:
                with blob.open("r") as f_in:
                    for i, line in enumerate(f_in):
                        if i >= num_rows:
                            break
                        f_out.write(line)
            logger.info("file streamed from gcp")
        except Exception as e:
            error_message="error in streamign file from GCP"
            logger.error(error_message)
            raise CustomException(error_message, e)
        
    
    def run(self):
        try:
            logger.info("Running the Data Ingestion process")
            #process
            self.download_csv_from_gcp()

        except CustomException as ce:
            logger.error(f"CustomerException: {str(ce)}")    
        finally:
            logger.info("Data ingestion run method ended")



if __name__=="__main__":
    config_file = read_yaml(CONFIG_PATH)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config_file["google_credentials_path"]


    data_ingestion=DataIngestion(config_file)
    data_ingestion.run()