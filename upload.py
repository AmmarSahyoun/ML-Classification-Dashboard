import streamlit as st
import pandas as pd





def GetFile():
    uploaded_file = st.file_uploader("", type="csv")
    if uploaded_file is not None:
        return (pd.read_csv(uploaded_file))


df = GetFile()

try:
    EA = GetFile(df)
    st.success('File successfully uploaded!')
