# Kyroform Multi-Omics Data Acquisition

A GUI-based web app for acquiring and curating multi-omics datasets for training HGNN models on gut microbiome–host PPIs in SLE.

## Features

- Fetch data from NCBI SRA, GEO, PRIDE, MetaboLights, HPIDB, STRING
- Curate and organize data for ML readiness
- Simple Streamlit GUI

## Installation

1. Clone or download the project.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Data Sources

- Metagenomics: NCBI SRA (e.g., SRP235678)
- Transcriptomics: GEO (e.g., GSE164457)
- Proteomics: PRIDE (e.g., PXD023456)
- Metabolomics: MetaboLights (e.g., MTBLS1234)
- PPI: HPIDB, STRING
- HGT: Precomputed from DarkHorse/MetaCHIP

## Extending to Other Diseases

Modify the dataset IDs in the app or add new modules for different APIs. Ensure paired samples and curation rules.

## Output Structure

Data saved in `data/` folder with subfolders for each omics type.