import requests
import pandas as pd

def fetch_ppi_data():
    """
    Fetch PPI data from STRING.
    Focus on host-microbial interactions.
    """
    # Example: get interactions for human and some microbes
    # For simplicity, query for human proteins
    url = "https://string-db.org/api/tsv/network"
    params = {
        "identifiers": "TP53\rBRCA1",  # example human proteins
        "species": 9606,
        "required_score": 400
    }
    response = requests.post(url, data=params)
    lines = response.text.strip().split("\n")
    data = [line.split("\t") for line in lines]
    df = pd.DataFrame(data[1:], columns=data[0])  # assuming header
    return df

def save_ppi(data, path='/home/satkrit/Downloads/Kyroform_RV/data/ppi/'):
    data.to_csv(path + 'ppi_data.csv', index=False)