import streamlit as streamlit
import pandas as pandas
import os
from io import BytesIO

st.set_page_config(page_title== "Data Sweeper",layout='wide')

#custom css
st.markdown(
    """
     <style>
     .stApp{
        background-color: black;
        color: white;
        }    
        </style>
        """,
        unsafe_allow_html=True
)

#title and description
st.title("Datasweeper Sterling Integrator By Kinza Shakil")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization Creating the project for quarter 3!")

#file uploader
uploaded_files = st.file_uploader("Upload your files (accepts CSV or Excel ):",type=["csv","xlsx"], accept_multiple_files=(True))

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

if file_ext == ".csv":
        df = pd.read_csv(file)
elif file_ext == "xlsx":
        df = pd.read_excel(file)
else:
        st.error(f"unsupported file type:{file_ext}")
continue
#file details
st.write("Preview the head of the Dataframe")
st.dataframe(df.head())
        
#data cleaning options
st.subheader("Data Cleaning Options")
if st.checkbox(f"clean data for {file.name}"):
    col1, col2 = st.columns(2)
    
with col1:
 if st.button(f"Remove duplicates from the file : {file.name}"):
 df.drop_duplicates(inplace=True)
 st.write("Duplicates removed!")

 with col2:
 if st.button(f"Fill missing values for {file.name}"):
 numeric_cols = df.select_dtypes(includes=['number']).columns
 df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
 st.write("Missing values have been filled!")

 st.subheader("select columns to keep")
 columns = st.multiselect(f"choose columns for {file.name}", df.columns, default=df.columns)
 df = df[columns]


        #data visualization
        st.subheader("data visualization")
        if st.checkbox(f"show visualization for {file.name}"):
            str.bar_chart(df.select_dtype2s(include='number').iloc[:, :2])

            #conversion options

            st.subheader("conversion options")
            conversion_type = st.radio(f"convert {file.name} to:", ["CVS" , "Excel"], key=file.name)
            if st.button(f"convert{file.name}"):
                buffer = BytesIO()
                if conversion_type == "CVS":
                    df.to.csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"

                    elif conversion_type == "excel":
                        df.to.to_excel(buffer, index=False)
                        file_name = file.name.replace(file_ext, ".xlsx")
                        mime_type = "applications/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    buffer.seek(0)       

                    st.download_button(
                        lablel=f"download {file.name} as {conversion_type}",
                        data=buffer,
                        file_name=file_name,
                        mime=mime_type
                    )
                    
st.success("All files processed successfully!")                                        
