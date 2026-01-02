import streamlit as st
from src import metagenomics, transcriptomics, proteomics, metabolomics, ppi, hgt, curation
import time

st.title("Kyroform Multi-Omics Data Acquisition")

# Inputs
st.header("Dataset Selection")
metagenomics_id = st.text_input("Metagenomics Project ID (SRA)", "SRP235678")
transcriptomics_id = st.text_input("Transcriptomics Dataset ID (GEO)", "GSE164457")
proteomics_id = st.text_input("Proteomics Project ID (PRIDE)", "PXD023456")
metabolomics_id = st.text_input("Metabolomics Study ID (MetaboLights)", "MTBLS1234")

progress_bar = st.progress(0)
status_text = st.empty()

if st.button("Fetch Data"):
    status_text.text("Starting data fetch...")
    progress_bar.progress(10)

    # Fetch metagenomics
    status_text.text("Fetching metagenomics data...")
    meta_data = metagenomics.fetch_metagenomics_data(metagenomics_id)
    progress_bar.progress(20)

    # Fetch transcriptomics
    status_text.text("Fetching transcriptomics data...")
    trans_expr, trans_meta = transcriptomics.fetch_transcriptomics_data(transcriptomics_id)
    progress_bar.progress(40)

    # Fetch proteomics
    status_text.text("Fetching proteomics data...")
    prot_data = proteomics.fetch_proteomics_data(proteomics_id)
    progress_bar.progress(50)

    # Fetch metabolomics
    status_text.text("Fetching metabolomics data...")
    metab_data = metabolomics.fetch_metabolomics_data(metabolomics_id)
    progress_bar.progress(60)

    # Fetch PPI
    status_text.text("Fetching PPI data...")
    ppi_data = ppi.fetch_ppi_data()
    progress_bar.progress(70)

    # Fetch HGT
    status_text.text("Fetching HGT data...")
    hgt_data = hgt.fetch_hgt_data()
    progress_bar.progress(80)

    # Curate
    status_text.text("Curating data...")
    curated = curation.curate_data(meta_data, (trans_expr, trans_meta), prot_data, metab_data, ppi_data, hgt_data)
    progress_bar.progress(90)

    # Save
    metagenomics.save_metagenomics(curated['metagenomics'])
    transcriptomics.save_transcriptomics(*curated['transcriptomics'])
    proteomics.save_proteomics(curated['proteomics'])
    metabolomics.save_metabolomics(curated['metabolomics'])
    ppi.save_ppi(curated['ppi'])
    hgt.save_hgt(curated['hgt'])

    progress_bar.progress(100)
    status_text.text("Data fetched and saved UwU")
    st.success("All data processed successfully UwU")

# Dashboard
st.header("Dataset Summary")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Metagenomics Samples", "100")  # placeholder
with col2:
    st.metric("Transcriptomics Samples", "50")
with col3:
    st.metric("Proteomics Samples", "30")

# Logs
st.header("Logs")
st.text_area("API Logs", "Logs here...", height=200)

# Export
if st.button("Export Datasets? UwU"):
    # Placeholder for zip export
    st.info("Export functionality: Download data from data/ folder")