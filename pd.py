import streamlit as st
import pandas as pd

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
new1 = pd.DataFrame()
new2 = pd.DataFrame()
new3 = pd.DataFrame()
new4 = pd.DataFrame()

uploaded_files = st.file_uploader("Choose a file", type=["xlsx"], accept_multiple_files=True)
if uploaded_files is not None:

    for uploaded_file in uploaded_files:
        df1 = pd.read_excel(uploaded_file, sheet_name= "Sheet1")
        new1 = new1.append(df1, ignore_index = True)
        df2 = pd.read_excel(uploaded_file, sheet_name= "Sheet2")
        new2 = new2.append(df2, ignore_index = True)
        # df3 = pd.read_excel(uploaded_file, sheet_name= "Sheet3")
        # new3 = new3.append(df3, ignore_index = True)
        # df4 = pd.read_excel(uploaded_file, sheet_name= "Sheet4")
        # new4 = new4.append(df4, ignore_index = True)
        

mergebtn = st.button("merge")
if mergebtn :
    
    writer = pd.ExcelWriter('new_file.xlsx')
    new1.to_excel(writer, sheet_name="Sheet1", index=False)
    new2.to_excel(writer, sheet_name="Sheet2", index=False)
    # new3.to_excel(writer, sheet_name="Sheet3", index=False)
    # new4.to_excel(writer, sheet_name="Sheet4", index=False)
    writer.save()
    writer.close()

    st.success("Merged successfully")

with open("new_file.xlsx", "rb") as file:
        st.download_button(
            label="Download Excel File",
            data=file,
            file_name='new_file.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )


