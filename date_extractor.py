import sqlite3
import pandas as pd
import os


def generate_date_database():
    # Link input and output files
    print("Generating Date Database ... ")
    input_file = 'form_responses.csv'
    output_file = 'entry_date.db'
    
    create_database(input_file, output_file)
    print("Timestamp Database Successfully Generated :-D ")
    
    
def create_database(input_file, output_file):
    # Delete Existing Database if exist
    if os.path.exists(output_file):
        os.remove(output_file)
     
    # Connecting to the new database 
    dest_db = sqlite3.connect(output_file)
    cursor = dest_db.cursor()
    
    # Creating new Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS records (Identification_Number INTEGER, Date INTEGER, Month INTEGER, Year INTEGER)''')
    
    # Extracting data
    db = pd.read_csv(input_file)
    processed_data = []
    for _, row in db.iterrows():
        id_number = row['Identification_Number']
        timestamp = row['Timestamp']
        
        # Filter missing timestamps
        db = db[db['Timestamp'].notna()]
        db = db[db['Timestamp'] != '']
        
        day, month, year = process_timestamp(timestamp)
        
        if year < 100:  # Normalize year value
            year += 2000
        
        processed_data.append((id_number, day, month, year))
        
    # Insert in new database
    cursor.executemany('''INSERT INTO records (Identification_Number, Date, Month, Year) VALUES (?, ?, ?, ?)''', processed_data)
    
    dest_db.commit()
    dest_db.close()
    
    print("Database created and data inserted successfully :-D \n")
    
    
def process_timestamp(timestamp):
    timestamp = str(timestamp)   # Convert timestamp to string

    if(timestamp == 'nan'):
        return 0, 0, 0
    # Split all these. Here, Year contains the time with it.
    month, day, year_time = timestamp.split('/')
    year = year_time.split(' ')[0]   # Extract year part
    return int(day), int(month), int(year)


def timestamp(timestamp):
    if(timestamp == 'nan'):
        return 0, 0, 0
    # Split all these. Here, Year contains the time with it.
    day, month, year_time = timestamp.split('/')
    year = year_time.split(' ')[0]   # Extract year part
    return int(day), int(month), int(year)