import os
import urllib.request
from carprice.custom_logging import logger

class GetData:
    def __init__(self):
        """_summary_

        """
        self.download_url = "https://raw.githubusercontent.com/aravind9722/datasets-for-ML-projects/main/cardekho_dataset.csv"
        self.train_data_dir = os.path.join("artifacts", "data")

    def initiate_download(self):
        

        os.makedirs(self.train_data_dir,exist_ok=True)
        filename = os.path.basename(self.train_data_dir)

        download_file_path = os.path.join(self.train_data_dir, filename)

        urllib.request.urlretrieve(self.download_url, download_file_path)


if __name__ == "__main__":
    obj = GetData()
    obj.initiate_download()
