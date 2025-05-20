import os
import requests
from urllib.parse import urlparse, parse_qs, unquote
from pathlib import Path

from src.config import *
from src.logger_config import setup_logger

logger = setup_logger('data.download_data', 'download_data.log')

def download_file(url, directory, fname=''):
    """
    Download a file from a given URL and save it to a directory.
    - inputs:
        - url: URL to request (string)
        - directory: a directory path (string) to save a downloaded file
        - fname: Optional. Specify a file name (string) to save it when it is 
            different from that contained in url.
    """
    # extract file name from URL
    file_name = get_filename_from_url(url)
    file_path = os.path.join(directory, file_name)
    
    # mimic a browser to avoid the status code 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # send a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # open a file in binary write mode and save the content to the file
        with open(file_path, 'wb') as file:
            file.write(response.content)
        logger.info(f"Downloaded {url} to {file_path}")
    else:
        logger.error(
            f"Failed to download {url} to {file_path}. Status code: {response.status_code}")


def download_dataset():
    """
    Download and save NPRI data listed in the config.py.
    """ 
    ensure_directory_exists(RAW_DIR)
    
    for name, url in DATA_URLS.items():
       download_file(url, RAW_DIR)


def ensure_directory_exists(directory: Path):
    """
    Ensure the directory exists; create it if it does not.
    """
    directory.mkdir(parents=True, exist_ok=True)


def get_filename_from_url(url: str) -> str:
    parsed = urlparse(url)

    # Case 1: Clean URL, like https://.../filename.csv
    if parsed.path.endswith('.csv'):
        return Path(parsed.path).name

    # Case 2: Query-style URL, like .../api/file?path=%2F...%2Ffilename.csv
    if parsed.query:
        query_params = parse_qs(parsed.query)
        if 'path' in query_params:
            return Path(unquote(query_params['path'][0])).name

    raise ValueError(f"Could not extract filename from URL: {url}")

