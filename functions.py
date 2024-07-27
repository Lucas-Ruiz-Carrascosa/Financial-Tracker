import streamlit as st

from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

expense_count = 0

expense_list = []



def total_expenses(expense_file_path="expenses.csv"):
    with open(expense_file_path,"r") as f:
        lines = len(list(f))
        return lines

def save_expense_to_file(name, amount, category, expense_file_path = "expenses.csv"):
    with open(expense_file_path, "a") as f:
        f.write(f"{date.today().day},{date.today().month}/{date.today().year}, {name}, {amount}, {category}, {date.today().year}\n")
        

def sumarize_expenses(budget, expense_file_path="expenses.csv"):
    
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            day, month_year, expense_name, expense_amount, expense_category, year = line.strip().split(",")
            expenses.append([day, month_year, expense_name, expense_amount, expense_category, year])

    amount_by_category = {}
    for expense in expenses:
        key = expense[4]
        if key in amount_by_category:
            amount_by_category[key] += float(expense[3])
        else: 
            amount_by_category[key] = float(expense[3])

    for key, amount in amount_by_category.items():
        st.write(f"  {key}: {amount:.2f}")
    
    amount_by_month = {}
    for expense in expenses:
        key = expense[1]
        if key in amount_by_month:
            amount_by_month[key] += float(expense[3])
        else:
            amount_by_month[key] = float(expense[3])

    #for key, amount in amount_by_month.items():
        #st.write(f"  {key}: {amount:.2f}")
    
    amount_by_year = {}
    for expense in expenses:
        key = expense[5]
        if key in amount_by_year:
            amount_by_year[key] += float(expense[3])
        else:
            amount_by_year[key] = float(expense[3])

    
    
    
    try:
        df = pd.DataFrame(list(amount_by_month.items()), columns=["Month/Year", "Total spending"])
        st.dataframe(df)
        st.line_chart(df, x="Month/Year", y="Total spending")
        df2 = pd.read_csv(expense_file_path, usecols=[5,3], header=None, names=["Total Spending", "Year"], dtype={"Year": str})
        
        st.bar_chart(df2, x="Year", y="Total Spending")
        df3 = pd.DataFrame(list(amount_by_year.items()), columns= ["Year", "Total spending"])
        st.dataframe(df3)
        
        

    except:
       st.write("To display charts the csv file must contain data")