import sqlite3
import pandas as pd
from prettytable import PrettyTable

import input_checker
import date_extractor


def overview_data():
    db = sqlite3.connect('financial_data.db')
    cursor = db.cursor()   
    view_data(db, cursor)  
    db.close()


def view_data(data_db, cursor):
    view = input_checker.check_input(["1", "2", "0"], "\nView Complete Data (1) \n     Query Search (2) \n     Exit (0) \n--->:")
    if(view == "1"):
        cursor.execute("SELECT * FROM finances WHERE Timestamp != 'NULL';")    
        rows = cursor.fetchall()
        
        # Print Data
        print_sql(cursor, rows)
        
        # Repeat
        print("\n")
        repeat = input_checker.check_input(["Y", "y", "N", "n"], "Have more queries (Y/n): ")
        if(repeat == "Y"):
            view_data(data_db, cursor)
            
        elif(repeat == "N"):
            print("\nExiting Query Search\n")

    elif(view == "2"):
        query_search(data_db, cursor)
    
    elif(view == "0"):
        print("\nExiting Query Search\n")

    
def query_search(data_db, cursor):
    print("\n")
    print("Enter 0 in any (Y/n) to start query search again.")
    print("Enter -1 in any (Y/n) to exit query search. \n")
 
    # Query Generation
    # Duration of Time
    duration_query = dur_query(data_db, cursor)  
    if(duration_query == "repeat"):
        return query_search(data_db, cursor)
    
    elif(duration_query == "abort"):
        return
    
    # Category of Expense
    category_query = cat_query(data_db, cursor) 
    if(category_query == "repeat"):
        return query_search(data_db, cursor)
    
    elif(category_query == "abort"):
        return
    
    # Type of Expense   
    type_query = typ_query(data_db, cursor) 
    if(type_query == "repeat"):
        return query_search(data_db, cursor)
    
    elif(type_query == "abort"):
        return
    
    # Amount Query
    amount_query = amt_query(data_db, cursor) 
    if(amount_query == "repeat"):
        return query_search(data_db, cursor)
    
    elif(amount_query == "abort"):
        return
    
    #Execute Query
    base = "SELECT * FROM finances"
    conditions = []

    # Add conditions
    if duration_query:
        conditions.append(duration_query)
    if category_query:
        conditions.append(category_query)
    if type_query:
        conditions.append(type_query)
    if amount_query:
        conditions.append(amount_query)
        
    # Final Query
    if conditions:
        query = f"{base} WHERE {' AND '.join(conditions)};"
    else:
        query = f"{base};"

    cursor.execute(query)
    rows = cursor.fetchall()
        
    # Print Data
    print_sql(cursor, rows)
        
    # Repeat
    print("\n")
    repeat = input_checker.check_input(["Y", "y", "N", "n"], "Have more queries (Y/n): ")
    if(repeat == "Y"):
        return view_data(data_db, cursor)
    
    elif(repeat == "N"):
        print("\nExiting Query Search\n")
        return


def print_sql(cursor, rows):
    # Put Column Desciption
    column = [description[0] for description in cursor.description]
    
    # Made a table using prettytable Library
    table = PrettyTable()
    table.field_names = column
    
    # Inserted Data in Table
    for row in rows:
        table.add_row(row)
        
    print(table)
    
    
def dur_query(data_db, cursor):
    # Setting Lower and Higher value of Timestamp
    enter = input_checker.check_input(["0", "-1", "Y", "y", "N", "n"], "Set Time Duration (Y/n): ")  
    if(enter == "0"):
        return "repeat"
    elif(enter == "-1"):
        return "abort"
    elif(enter == "N"):
        return ""
    
    elif(enter == "Y"):
        print("\n")
        print("Format of Entry (DD/MM/YYYY) or (DD/MM/YY)")
        
        low = input_checker.date_input("From (Can leave to select complete data) : ")
        if(low == ""):
            low = "01/01/2024"
            
        high = input_checker.date_input("To (Can leave empty to select today): ")
        if(high == ""):
            high = "01/01/2099"
        
    # Query Duration
    l_date, l_month, l_year = date_extractor.timestamp(low)
    h_date, h_month, h_year = date_extractor.timestamp(high)
    
    # Connect to time database
    time_db = sqlite3.connect("entry_date.db")
    time_cursor = time_db.cursor()
    
    try:
        query_date = f"SELECT Identification_Number FROM records WHERE (Year > {l_year} AND Year < {h_year}) OR (Year = {l_year} AND ((Month > {l_month}) OR (Month = {l_month} AND Date >= {l_date})) OR (Year = {h_year} AND (Month < {h_month}) OR (Month = {h_month} AND Date <= {h_date})));" 
        result = pd.read_sql_query(query_date, time_db)
        
        id_all = result['Identification_Number'].tolist()
        
        # If no data found
        if not id_all:
            print(f"No records for the date: From {l_date}/{l_month}/{l_year} to {h_date}/{h_month}/{h_year}")
            
        
        # Flatten list of Tuples
        id_string = ", ".join(map(str, id_all))
        
        # Query
        duration_query = f"Identification_Number IN ({id_string})"
        
    finally:
        # Close Database
        time_db.close() 
        
    return duration_query
    
    
def typ_query(data_db, cursor):
    # Type of Expense
    enter = input_checker.check_input(["0", "-1", "Y", "y", "N", "n"], "Set Type of Expense (Y/n): ")
    if(enter == "0"):
        return "repeat"
    elif(enter == "-1"):
        return "abort"
    elif(enter == "N"):
        return ""
    
    elif(enter == "Y"):
        print("\nType of Expense: ")
        print("Leave field to select all type")
        print("         1. Foodings")
        print("         2. Lending")
        print("         3. Credit")
        print("         4. Personal")
        print("         5. Travel")
        print("         6. Recharge")
        print("         7. Others")
        typ = input_checker.check_input(["", "1", "2", "3", "4", "5", "6", "7"], "-------> : ")
        if(typ == ""):
            typ = "9"
    
    # Query Generation
    if(typ == "1"):
        type_query = "AND Type of Expense: = 'Foodings' AND"
    elif(typ == "2"):
        type_query = "[Type of Expense:] = 'Lending'"
    elif(typ == "3"):
        type_query = "[Type of Expense:] = 'Credit'"
    elif(typ == "4"):
        type_query = "[Type of Expense:] = 'Personal'"
    elif(typ == "5"):
        type_query = "[Type of Expense:] = 'Travel'"
    elif(typ == "6"):
        type_query = "[Type of Expense:] = 'Recharge'"
    elif(typ == "7"):
        type_query = "[Type of Expense:] = 'Others'"
    elif(typ == "9"):
        type_query = ""
    
    return type_query


def cat_query(data_db, cursor):
    # Category of Expense Query
    enter = input_checker.check_input(["0", "-1", "Y", "y", "N", "n"], "Set Category (Debit / Credit) (Y/n): ")
    if(enter == "0"):
        return "repeat"
    elif(enter == "-1"):
        return "abort"
    elif(enter == "N"):
        return ""
    
    elif(enter == "Y"):
        print("Leave to select both")
        print("         1. Debit")
        print("         2. Credit")
        category = input_checker.check_input(["", "1", "2"], "-------> : ")
        if(category == ""):
            category = "9"
    
    # Query Generation
    if(category == "1"):
        category_query = "[Categorization of Expense:] = 'Debit'"
    elif(category == "2"):
        category_query = "[Categorization of Expense:] = 'Credit'"
    elif(category == "9"):
        category_query = ""
        
    return category_query


def amt_query(data_db, cursor):
    #Amount range
    enter = input_checker.check_input(["0", "-1", "Y", "y", "N", "n"], "Set amount range (Y/n): ")
    if(enter == "0"):
        return "repeat"
    elif(enter == "-1"):
        return "abort"
    elif(enter == "N"):
        return ""
    
    elif(enter == "Y"):
        print("Leave lower limit blank to set it to 0.")
        ruplow = input_checker.amount_input("Enter lower limit: ")
        if(ruplow == -1):
            ruplow = 0
            
        print("Leave high limit to select all.")
        ruphigh = input_checker.amount_input("Enter higher limit: ")
        if(ruphigh == -1):
            ruphigh = 9999999
        
    # Query Generation
    amount_query = f"[Amount of Expense: in ₹] >= {ruplow} AND [Amount of Expense: in ₹] <= {ruphigh}"
    
    return amount_query
              
        
    