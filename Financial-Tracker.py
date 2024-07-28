import pandas as pd
import streamlit as st
import functions as func
from datetime import date
datafile = None
st.title("Financial tracker")

tab1, tab2 = st.tabs(["Expenses", "History"])
with tab1:
    
    st.header("Here you can track your expenses for this month")
    st.subheader("Upload a csv file, you can download an updated version when you have finnished using the app.")
    csv_file = st.file_uploader("This file is generated from this website, and is used to keep track of previous financial info. You can download the updated file from here as well", "csv")
    if csv_file:
        datafile = pd.read_csv(csv_file, header=None)
        if "key" not in st.session_state:
            st.session_state["key"] = datafile
        
        
    else:
        pass
    if "key" in st.session_state:
        st.download_button("Download updated csv", st.session_state.key.to_csv(header=None, index=False), "Expense_file.csv")
    budget = float(st.text_input("Enter your budget", 0))
    
    
    expense_name = st.text_input("Enter the expense name: ")
    expense_amount = st.number_input("Enter the expense amount: ")
    category = st.selectbox("What is the category of you purchase?",
                            ("Food", "Home", "Work", "Fun", "Sport", "Misc"))
    if st.button("Submit"): #and csv_file:
        
        if expense_amount:
            expense_amount = float(expense_amount)
            expense_amount = round(expense_amount, 3)
            
            
            #save_expense_to_file(expense_name, expense_amount, category)
            st.session_state.key.loc[len(st.session_state.key)] = [date.today().day, f"{date.today().month}/{date.today().year}", expense_name, expense_amount, category, date.today().year]
            st.write(f"You've added {expense_name} ({expense_amount}) to your expenses.")
            st.write(f"You have {func.total_expenses(st.session_state.key)} expenses.")
            
            
            
        else: 
            st.write("Make sure an ammount is specified")
    elif csv_file is None:
        st.write("Make sure you have a csv file")
    if st.button("Sumarize"):
        st.header("Expense summary")
        st.write("Note, the values shown when hovering over the graph represent to all the individual purchases, not to the total for the month")
        if "key" in st.session_state:
            func.sumarize_expenses(budget, st.session_state.key)
        else:
            st.write("Make sure you have added a csv file")
   
with tab2:
    st.header("This is a view of all your historical data")
    if st.button("Show all data") and "key" in st.session_state:
        st.dataframe(st.session_state.key)

    if st.button("Graph/Chart View"):
        st.header("Graphs/Charts")
        st.write("When hovering over the bar chart, the total displayed is the total in that purchase not the year, to see the total for the year refer to the chart (bottom of the page)")
        try:
                func.sumarize_expenses(budget, st.session_state.key)
        except:
            st.write("To display charts the csv file must contain data")



    

