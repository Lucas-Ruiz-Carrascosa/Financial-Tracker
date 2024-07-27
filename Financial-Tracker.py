import pandas as pd
import streamlit as st
import functions as func

st.title("Financial tracker")

tab1, tab2 = st.tabs(["Expenses", "History"])
with tab1:
    
    st.header("Here you can track your expenses for this month")
    st.subheader("Upload a csv file, you can download an updated version when you have finnished using the app.")
    csv_file = st.file_uploader("This file is generated from this website, and is used to keep track of previous financial info. You can download the updated file from here as well", "csv")
    if csv_file:
        #Saving file
        with open(csv_file.name, "wb") as f:
            f.write(csv_file.getbuffer())
        st.download_button("Download csv", csv_file, "expenses.csv")
    else:
        pass
    budget = float(st.text_input("Enter your budget", 0))
    
    
    expense_name = st.text_input("Enter the expense name: ")
    expense_amount = st.number_input("Enter the expense amount: ")
    category = st.selectbox("What is the category of you purchase?",
                            ("Food", "Home", "Work", "Fun", "Sport", "Misc"))
    if st.button("Submit") and csv_file:
        with open(csv_file.name, "a") as f:
            if expense_amount:
                expense_amount = float(expense_amount)
                expense_amount = round(expense_amount, 3)
            
            
                func.save_expense_to_file(expense_name, expense_amount, category, csv_file.name)
                st.write(f"You've added {expense_name} ({expense_amount}) to your expenses.")
                st.write(f"You have {func.total_expenses(csv_file.name)} expenses.")
            
            
            else: 
                st.write("Make sure an ammount is specified")
    elif csv_file is None:
        st.write("Make sure you have a csv file")
    if st.button("Sumarize"):
        st.header("Expense summary")
        st.write("Note, the values shown when hovering over the graph represent to all the individual purchases, not to the total for the month")
        if csv_file:
            func.sumarize_expenses(budget, csv_file.name)
        else:
            st.write("Make sure you have added a csv file")
   
with tab2:
    st.header("This is a view of all your historical data")
    if st.button("Show all data"):
        try:
            dataframe = pd.read_csv(csv_file.name, header=None, names=["Day", "Month/Year", "Name", "Price", "Category", "Year"], dtype={"Year": str})
            st.dataframe(dataframe)
        except:
            st.write("Make sure there is a file and it has some data")
    if st.button("Graph/Chart View"):
        st.header("Graphs/Charts")
        st.write("When hovering over the bar chart, the total displayed is the total in that purchase not the year, to see the total for the year refer to the chart (bottom of the page)")
        try:
                func.sumarize_expenses(budget, csv_file.name)
        except:
            st.write("To display charts the csv file must contain data")
    


