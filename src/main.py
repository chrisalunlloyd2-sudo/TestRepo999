import os
import sys
from utils import data_ingestion, data_processing, data_visualization

def main():
    # Data ingestion
    data = data_ingestion()
    
    # Data processing
    processed_data = data_processing(data)
    
    # Data visualization
    data_visualization(processed_data)

if __name__ == "__main__":
    main()
