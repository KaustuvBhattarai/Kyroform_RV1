import GEOparse
import pandas as pd

def fetch_transcriptomics_data(dataset_id='GSE164457'):
    """
    Fetch transcriptomics data from GEO.
    """
    gse = GEOparse.get_GEO(dataset_id)
    # Get expression matrix
    try:
        expression = gse.pivot_samples('VALUE')
    except KeyError:
        # If 'ID_REF' not found, try to pivot with different index
        data = []
        for gsm_name, gsm in gse.gsms.items():
            df = gsm.table
            if df.empty or len(df.columns) == 0:
                continue  # Skip empty tables
            # Find ID column (first column or 'ID_REF' if exists)
            id_col = df.columns[0] if 'ID_REF' not in df.columns else 'ID_REF'
            # Find value column (numeric column, not ID)
            value_col = None
            for col in df.columns:
                if col != id_col and df[col].dtype in ['float64', 'int64']:
                    value_col = col
                    break
            if value_col is None:
                continue  # No numeric column
            df_pivot = df[[id_col, value_col]].copy()
            df_pivot["name"] = gsm_name
            df_pivot.rename(columns={value_col: 'VALUE'}, inplace=True)
            data.append(df_pivot)
        if data:
            expression = pd.concat(data).pivot(index=id_col, values='VALUE', columns="name")
        else:
            expression = pd.DataFrame()  # Empty if no data
    
    # Metadata
    metadata = gse.phenotype_data
    return expression, metadata

def save_transcriptomics(expression, metadata, path='/home/satkrit/Downloads/Kyroform_RV/data/transcriptomics/'):
    expression.to_csv(path + 'expression_matrix.csv')
    metadata.to_csv(path + 'sample_metadata.csv')