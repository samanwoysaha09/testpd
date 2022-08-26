import streamlit as st
import pandas as pd

df1 = pd.DataFrame()
new1 = pd.DataFrame()
uploaded_files = st.file_uploader("Choose a file", type=["xlsx"], accept_multiple_files=True)
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        df1 = pd.read_excel(uploaded_file, sheet_name= "Sheet1")
        new1 = new1.append(df1, ignore_index = True)
        
    st.write(new1)
mergebtn = st.button("merge")
if mergebtn :
    new1.to_excel("new_file.xlsx", sheet_name="Sheet1", index=False)
    st.success("Merged successfully")


