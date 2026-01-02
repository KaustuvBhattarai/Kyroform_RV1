import requests
import pandas as pd

def fetch_metabolomics_data(study_id='MTBLS1234'):
    """
    Fetch metabolomics data from MetaboLights.
    """
    url = f"https://www.ebi.ac.uk/metabolights/ws/studies/{study_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return {}
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return {}
    return data

def save_metabolomics(data, path='/home/satkrit/Downloads/Kyroform_RV/data/metabolomics/'):
    if isinstance(data, dict):
        pd.DataFrame([data]).to_csv(path + 'metabolomics_data.csv')
    else:
        pd.DataFrame(data).to_csv(path + 'metabolomics_data.csv')