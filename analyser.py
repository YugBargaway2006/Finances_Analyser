import sqlite3
import colorama
import pandas as pd
from sqlalchemy import create_engine

import queries


def load_db():
    # Using Pandas to read and analyse csv file
    print("Loading csv in memory ...")
    data = pd.read_csv('form_responses.csv')
    print("Successfully Done :-D \n")
    
    # Connect SQL Database
    print("Linking .db file ...")
    engine = create_engine('sqlite:///financial_data.db')
    print("Successfully Done :-D \n")
    
    # Import Data
    print("Importing Data ...")
    data.to_sql('finances', engine, if_exists='replace', index=False)
    print("Successfully Done :-D \n")
    
    
def credit_debit(db):
    expenses = db[db['Categorization of Expense:'] == 'Debit']['Amount of Expense: in ₹'].sum()
    income = db[db['Categorization of Expense:'] == 'Credit']['Amount of Expense: in ₹'].sum()
    balance = income - expenses
    
    print("\nTotal Credit till now:              ", end="")
    print(colorama.Fore.GREEN + f"{income}" + colorama.Fore.WHITE)
    print("Total Expenses till now:            ", end="")
    print(colorama.Fore.RED + f"{expenses}" + colorama.Fore.WHITE)
    if(balance > 0):
        print("\nRemaining Balance:                  ", end="")
        print(colorama.Fore.GREEN + f"{balance}\n" + colorama.Fore.WHITE)
    else:
        print("\nRemaining Balance:                  ", end="")
        print(colorama.Fore.RED + f"{balance}\n" + colorama.Fore.WHITE)
    

def diversify_credit_debit(db):
    # Group on basis of Expense
    expenses = db[db['Categorization of Expense:'] == 'Debit'].groupby('Type of Expense:')['Amount of Expense: in ₹'].sum()
    income = db[db['Categorization of Expense:'] == 'Credit'].groupby('Type of Expense:')['Amount of Expense: in ₹'].sum()
    
    # Printing expenses 
    print("\nExpenses by Category:") 
    print(expenses) 
    
    # Printing income 
    print("\nIncome by Category:") 
    print(income)
    

def monthly_trends(db):
    # Load Date SQL Database
    date_db = sqlite3.connect('entry_date.db')
    sql_date = pd.read_sql_query("SELECT * FROM records", date_db)
    date_db.close()
    
    # Merge both on Identification Number
    merged_db = pd.merge(db, sql_date, on='Identification_Number', how='inner')
    
    # Group by Month and Year
    monthly_expenses = merged_db[merged_db['Categorization of Expense:'] == 'Debit'].groupby(['Year', 'Month'])['Amount of Expense: in ₹'].sum()
    
    print("\nMonthly Expenses: ")
    print(monthly_expenses)
    
    

def type_analysis(db):
    expenses = db[db['Categorization of Expense:'] == 'Debit'].groupby('Type of Expense:')['Amount of Expense: in ₹'].sum()
    total_expenses = db[db['Categorization of Expense:'] == 'Debit']['Amount of Expense: in ₹'].sum()
    category_percentages = (expenses / total_expenses) * 100
    
    # Print Expenses and Percentage
    print("\nExpenses by Category:") 
    print(expenses) 

    print("\nPercentage by Category:") 
    print(category_percentages)
    

def outlier_detection(db):
    # Deviation from Mean
    up_limit = db['Amount of Expense: in ₹'].mean() * 1.75
    
    # Query Generation and flush
    sql_db = sqlite3.connect('financial_data.db')
    cursor = sql_db.cursor()
    query = f"SELECT * FROM finances WHERE [Amount of Expense: in ₹] >= {up_limit};"
    cursor.execute(query)
    rows = cursor.fetchall()
        
    # Print Data
    queries.print_sql(cursor, rows)
    
    
def savings_potential(db):
    # Load Date SQL Database
    date_db = sqlite3.connect('entry_date.db')
    sql_date = pd.read_sql_query("SELECT * FROM records", date_db)
    date_db.close()
    
    # Merge both on Identification Number
    merged_db = pd.merge(db, sql_date, on='Identification_Number', how='inner')
    
    # Group by Month and Year
    monthly_expenses = merged_db[merged_db['Categorization of Expense:'] == 'Debit'].groupby(['Year', 'Month'])['Amount of Expense: in ₹'].sum()
    monthly_credit = merged_db[merged_db['Categorization of Expense:'] == 'Credit'].groupby(['Year', 'Month'])['Amount of Expense: in ₹'].sum()
    
    savings = monthly_credit - monthly_expenses
    print("\nSavings Potential: ")
    print(savings)
    