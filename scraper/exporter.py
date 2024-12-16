import pandas as pd
import logging

def export_to_csv(data, filename = "jobs_data.csv"):
    """
    Export job data to csv format

    Args:
        data (list[dict]): list of job data
        filename (str): Name of the CSV file to save.
    """
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to export data to {filename}: due to {e}")
