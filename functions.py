import streamlit as st

from datetime import date
import pandas as pd


expense_count = 0

expense_list = []



def total_expenses(datafile):
    return len(datafile)


    
        

def sumarize_expenses(budget, datafile):
    
    expenses = []
    
    for index, rows in datafile.iterrows():
        my_list =[rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]]
        expenses.append(my_list)

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

        
        df3 = pd.DataFrame(list(amount_by_year.items()), columns= ["Year", "Total spending"])
        st.bar_chart(df3, x="Year", y="Total spending")
        st.dataframe(df3)
        
        

    except:
       st.write("To display charts the csv file must contain data")
