import pandas as pd

import csv_extractor
import analyser
import queries
import input_checker
import date_extractor


def main():
    csv_url = "<csv_url> (README.md)"
    if(csv_url == "<csv_url> (README.md)"):
        print("\nEnter csv_url first in the Financial_Analyser.py")
        print("Method to setup google form for responses and extracting link is provided in README.md")
        print("DO Read :-D")
        print("Exiting ...\n")
        out = input("Click Enter to exit ")
        return
    
    csv_extractor.save_csv(csv_url)  # Save form responses as .csv file
    analyser.load_db()    # Convert .csv to .db file
    date_extractor.generate_date_database()  # Generate Timestamp database
    
    while(True):
        view = input_checker.check_input(["Y", "y", "N", "n"], "\nView Data (Y/n): ")  # View Data
        if(view == "Y"):
            queries.overview_data()
            
        analyse = input_checker.check_input(["Y", "y", "N", "n"], "\nAnalyze Data (Y/n): ")
        
        if(analyse == "Y"):
            # Load Database
            db = pd.read_csv('form_responses.csv')
            
            # Sum all debit and credit information
            cat_sum = input_checker.check_input(["Y", "y", "N", "n"], "\nSum Data on Credit and Debit (Y/n): ")
            if(cat_sum == "Y"):
                analyser.credit_debit(db)
                print("\n")
            
            # Categorize all credit and debit information
            cat_dc = input_checker.check_input(["Y", "y", "N", "n"], "Diversify Data on Credit and Debit (Y/n): ")
            if(cat_dc == "Y"):
                analyser.diversify_credit_debit(db)
                print("\n")
            
            # Categorize expenses on basis of type
            cat_typ = input_checker.check_input(["Y", "y", "N", "n"], "\nDiversify Data on Type of Expense (Y/n): ")
            if(cat_typ == "Y"):
                analyser.type_analysis(db)
                print("\n")
                
            # Categorize expenses on basis of Month
            cat_typ = input_checker.check_input(["Y", "y", "N", "n"], "\nDiversify Data on Monthly Basis (Y/n): ")
            if(cat_typ == "Y"):
                analyser.monthly_trends(db)
                print("\n")
                
            outl = input_checker.check_input(["Y", "y", "N", "n"], "\nFlag unusually high transaction (Y/n): ")
            if(outl == "Y"):
                analyser.outlier_detection(db)
                print("\n")
                
            sav = input_checker.check_input(["Y", "y", "N", "n"], "\nCalculate Savings Potential (Y/n): ")
            if(sav == "Y"):
                analyser.savings_potential(db)
                print("\n")
                

        elif(analyse == "N"):
            print("\nQuiting Program ...")
            print("Thanks for Using :-D")
            print("Have a great day ahead!\n")
            break
        
        repeat = input_checker.check_input(["Y", "y", "N", "n"], "\nView Data (Y/n): ")
        if(repeat == "N"):
            break
            
           
main()