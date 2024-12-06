import requests
import pandas as pd
import os


def save_csv(csv_url):
    # Replace with your Google Sheet's published CSV URL
    save_path = "form_responses_without_id.csv"   
    print("\nDownloding .csv file of responses ...") 
    extract_csv(csv_url, save_path)
    

def extract_csv(csv_url, save_path):
    try:
        # Fetch CSV data
        response = requests.get(csv_url)
        response.raise_for_status()  # Raise an erro for bad HTTP status codes
        
        # Save the data to a local file
        with open(save_path, 'wb') as file:
            file.write(response.content)
            
        print(f"CSV file download successfully as '{save_path}'! \n")
        
        # Add Identification_Number
        add_id()
        
    except requests.exceptions.RequestException as err:
        # Not able to download csv file of responses
        print(f"Failed to download CSV: {err}")
        

def add_id():
    csv_file = "form_responses_without_id.csv"
    output_file = "form_responses.csv"
    
    db = pd.read_csv(csv_file)
    
    # Add a table Identification Number
    db.insert(0, 'Identification_Number', range(1, len(db) + 1))

    # Delete Existing Database if exist
    if os.path.exists(output_file):
        os.remove(output_file)
        
    # Save file
    db.to_csv(output_file, index=False)
    
    # Remove old csv
    if os.path.exists(csv_file):
        os.remove(csv_file)
    
    print(f"File saved with index column as '{output_file}'\n")
    
    
        
