from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# key directories
DATA_DIR = PROJECT_ROOT / 'data'
CONFIG_DIR = DATA_DIR / 'config'
RAW_DIR = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'
OUTPUT_IMG_DIR = PROJECT_ROOT / 'output_images'

# key file
DATA_URLS = {
    'geolocation': 'https://data-donnees.az.ec.gc.ca/api/file?path=%2Fsubstances%2Fplansreports%2Freporting-facilities-pollutant-release-and-transfer-data%2Fbulk-data-files-for-all-years-releases-disposals-transfers-and-facility-locations%2FNPRI-INRP_GeolocationsGeolocalisation_1993-present.csv',
    'releases': 'https://data-donnees.az.ec.gc.ca/api/file?path=%2Fsubstances%2Fplansreports%2Freporting-facilities-pollutant-release-and-transfer-data%2Fbulk-data-files-for-all-years-releases-disposals-transfers-and-facility-locations%2FNPRI-INRP_ReleasesRejets_1993-present.csv',
    'disposals': 'https://data-donnees.az.ec.gc.ca/api/file?path=%2Fsubstances%2Fplansreports%2Freporting-facilities-pollutant-release-and-transfer-data%2Fbulk-data-files-for-all-years-releases-disposals-transfers-and-facility-locations%2FNPRI-INRP_DisposalsEliminations_1993-present.csv',
    'transfers': 'https://data-donnees.az.ec.gc.ca/api/file?path=%2Fsubstances%2Fplansreports%2Freporting-facilities-pollutant-release-and-transfer-data%2Fbulk-data-files-for-all-years-releases-disposals-transfers-and-facility-locations%2FNPRI-INRP_DisposalsEliminations_TransfersTransferts_1993-present.csv',
}
