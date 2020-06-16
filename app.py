import streamlit as st
import pandas as pd
import mushromm
import about
import UploadFile
from PIL import Image


def main():
    menu = ['About', 'Mushroom data', 'Upload dataset']
    menuSelection = st.sidebar.radio('', menu, index=0, key=None)

    if menuSelection == 'About':
        header()
        about.display_about()
        about.display_contribute()
        if st.sidebar.button("Many thanks"):
            st.balloons()

    if menuSelection == 'Upload dataset':
        st.success("# _Model Hints_Web App_ `version0.0.1` ")
        st.markdown("<h1 style = 'text-align: center; color: green;' > 3-Models of Binary Classification </ h1>",
                    unsafe_allow_html=True)
        st.markdown("<h3 style = 'text-align: center; color: Blue;' >  📁Uplaod CSV file  </ h3>",
                    unsafe_allow_html=True)
        uploadFile()

    if menuSelection == 'Mushroom data':
        header()
        mushromm.mushroomSetup()


def header():
    st.success("# _Model Hints_Web App_ `version0.0.1` ")
    st.markdown("<h1 style='text-align: center; color:green;'> 3-Models of Binary Classification </ h1>",
                unsafe_allow_html=True)
    img = Image.open("./templates/mushroom.jpg")
    st.image(img)
    st.header(" **🍄Are your mushrooms edible or poisonous?🍄**")


def uploadFile():
    uploaded_file = st.file_uploader("", type="csv")
    if uploaded_file is not None:
        dataFrame = pd.read_csv(uploaded_file)

    try:
        uploadedData = UploadFile.FileInfo(dataFrame)
        st.success('Successfully uploaded!')

        st.title('Select a function:')
        dfInfo = st.selectbox("", ['Head', 'Describe', 'Info', 'Isnull', 'Unique values and iteration'])

        if dfInfo == 'Head':
            st.subheader('Dataframe head:')
            st.write(dataFrame.head())

        if dfInfo == 'Describe':
            st.subheader('Dataframe description:')
            st.write(dataFrame.describe())

        if dfInfo == 'Info':
            st.subheader('Dataframe informations:')
            st.text(uploadedData.info())

        if dfInfo == 'Isnull':
            st.subheader('Null occurrences')
            st.write(dataFrame.isnull().sum())

        if dfInfo == 'Unique values and iteration':
            col = st.selectbox('Choose a column to see unique values', uploadedData.columns)
            st.subheader('Unique values and iteration')
            st.write(uploadedData.info2(col))

    except:
        st.error('Upload a CSV file to get started.')


if __name__ == '__main__':
    main()
