# FINANCIAL TRACKER
#### Video Demo:  <URL HERE>
#### Description: This program takes input through google forms of financial information of a person. It, then, converts it into database file. The program helps view complete data and also on certain queries regarding timeframe, credit/debit, etc. The Program also analyses it by printing sum of data using certain queries. It also contains the function to find unusual high transactions.

## TABLE OF CONTENTS:
### 1. Requirement Modules
### 2. Setting Initial Google forms
### 3. Settings for Google Sheets to set beforhand
### 4. Configuration
### 5. Maintainer

### 1. Requirement Modules:
You can run the program by running Financial_Analyser.py on your system.
Do first create a google form and link the .csv file for proper functioning of the program.
The following python modules are required for proper functioning and execution of the program,
- Pandas: For Handling csv database and its queries
- Colorama: Required for coloring letters in terminal window
- sqlalchemy: Handles sql commands and .db files using python window
- requests: Required for downloading form_responses from the web
- PrettyTable: Handles printing of sql queries in a table fashion
- Sqlite3: Required for loading .db in memory and running sql queries on it
- os: Handles creation and deletion of files in the directory

Sqlite3 and OS modules comes in-built with the python module.
All other modules can be downloaded by running Requirements.py once.


### 2. Setting Initial Google Form:
Use the following method to setup the form correctly so as not to mess up with the column names of csv database, then generated.
1. Goto forms.google.com
2. Heading of Questions are as follows:
    - [<Column Name>] (Type) Options

    - [Categorization of Expense:] (Multiple Choice) Debit , Credit

    - [Type of Expense:] (Dropdown) 
                          1. Foodings
                          2. Lending
                          3. Credit
                          4. Personal
                          5. Travel
                          6. Recharge
                          7. Other

    - [Expense Desciption:] (Short Answer)

    - [Amount of Expense: in ₹] (Short Answer , Number)

3. Goto to responses tab and click on Link to spreadsheet to make a google sheet of the responses.


### 3. Setting for Google Sheet to set beforehand
The link of .csv file of spreadsheet is need to be generated to access it from the python code.
1. Set the spreadsheet to view only with anyone with the link.
2. Goto File -> Share -> Publish to Web -> Select Entire Document, Comma Seperated Values (.csv) -> Copy Link
3. Paste the link in Financial_Analyser.py in place csv_url variable.


### 4. Configuration:
The Code has many different functions for the analysis of the financial information provided.
The First Section focuses on printing the data on the console, either completely or with the help of certain queries regarding, 
    - Time Duration
    - Category (Debit / Credit)
    - Type of Expense 
    - Amount
The Implementation of Time Duration involves the creation of new database with date information of transactions as google form timestamp is not in the correct required format.
An extra column with Identification Number is created for linking of the two database.

The Further section of the code focuses more on analysis of the data, and giving output based on certain categories.
This section analyses data on the basis of, 
    - Credit and Debit and Outstanding balance
    - Types of Expenses
    - Monthly Expenses
    - Finding unusually high transactions
    - Saving Potential of each month
The Unusually high transaction values are those whose amount is greater than 1.75 x (Mean Value of Amounts)


### 5. Maintainer:
This Code is completely made from Scratch by Yug Bargaway, with certain references taken from various websites for debugging and resolving queries. 
All rights of this code is reserved only for Yug Bargaway.

Publishing or Circulating this code, either physically or digitally, by any means possible without the consent of the owner (Yug Bargaway) is strictly prohibited and punishable.
Kindly refrain from any of these activities.


