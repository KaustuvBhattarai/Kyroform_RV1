import pandas as pd
from Bio import Entrez
import xml.etree.ElementTree as ET

def fetch_metagenomics_data(project_id='SRP235678'):
    """
    Fetch metagenomics data from NCBI SRA using Biopython and ElementTree.
    Returns metadata for samples.
    """
    Entrez.email = "your.email@example.com"  # Set your email
    # Search for the project
    handle = Entrez.esearch(db="sra", term=project_id)
    record = Entrez.read(handle)
    handle.close()
    
    ids = record["IdList"]
    if not ids:
        return pd.DataFrame()
    
    # Fetch metadata as XML
    handle = Entrez.efetch(db="sra", id=",".join(ids), rettype="xml")
    xml_data = handle.read()
    handle.close()
    
    # Parse XML with ElementTree
    root = ET.fromstring(xml_data)
    
    # Parse to DataFrame
    data = []
    for exp_package in root.findall('.//EXPERIMENT_PACKAGE'):
        sample = exp_package.find('.//SAMPLE')
        exp = exp_package.find('.//EXPERIMENT')
        run = exp_package.find('.//RUN')
        if sample is not None and exp is not None:
            data.append({
                'sample_id': sample.get('accession', ''),
                'experiment_id': exp.get('accession', ''),
                'run_id': run.get('accession', '') if run is not None else '',
                'title': sample.findtext('.//TITLE', ''),
                'organism': sample.findtext('.//SCIENTIFIC_NAME', ''),
                'platform': exp.findtext('.//INSTRUMENT_MODEL', ''),
            })
    df = pd.DataFrame(data)
    return df

# Save to CSV
def save_metagenomics(data, path='/home/satkrit/Downloads/Kyroform_RV/data/metagenomics/'):
    data.to_csv(path + 'metagenomics_metadata.csv', index=False)