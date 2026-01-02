import requests
import pandas as pd

def fetch_proteomics_data(project_id='PXD023456'):
    """
    Fetch proteomics data from PRIDE.
    """
    url = f"https://www.ebi.ac.uk/pride/ws/archive/v2/projects/{project_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return {}  # Project not found or error
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return {}  # Not JSON response
    return data

def save_proteomics(data, path='/home/satkrit/Downloads/Kyroform_RV/data/proteomics/'):
    # Save as JSON or CSV
    if isinstance(data, dict):
        pd.DataFrame([data]).to_csv(path + 'proteomics_data.csv')
    else:
        pd.DataFrame(data).to_csv(path + 'proteomics_data.csv')