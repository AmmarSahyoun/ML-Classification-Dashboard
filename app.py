import streamlit as st
import pandas as pd
import mushromm
import about
import UploadFile
from PIL import Image


def main():
    menu = ['Mushroom data', 'About', 'Upload dataset']
    menuSelection = st.sidebar.radio('', menu, index=1, key=None)

    if menuSelection == 'About':
        header()
        about.display_about()
        about.display_contribute()
        if st.sidebar.button("Many thanks"):
            st.balloons()

    if menuSelection == 'Upload dataset':
        st.success("# _Model Hints_Web App_ `version0.0.1` ")
        st.title("3-Models of Binary Classification")
        st.header(" **📁Uplaod CSV file**")
        uploadFile()



    if menuSelection == 'Mushroom data':
        header()
        mushromm.mushroomSetup()

def header():
    st.success("# _Model Hints_Web App_ `version0.0.1` ")
    st.title("3-Models of Binary Classification")
    img = Image.open("./templates/mushroom.jpg")
    st.image(img)
    st.header(" **🍄Are your mushrooms edible or poisonous?🍄**")

def uploadFile():
    uploaded_file = st.file_uploader("", type="csv")
    if uploaded_file is not None:
        dataFrame = pd.read_csv(uploaded_file)

    try:
        EA = UploadFile.FileInfo(dataFrame)
        st.success('Successfully uploaded!')

        st.title('Dataframe basic informations')

        st.sidebar.subheader('Basica exploratory analysis options')
        if st.sidebar.checkbox('Basic informations'):

            if st.sidebar.checkbox('Head'):
                st.subheader('Dataframe head:')
                st.write(dataFrame.head())

            if st.sidebar.checkbox('Describe'):
                st.subheader('Dataframe description:')
                st.write(dataFrame.describe())

            if st.sidebar.checkbox('Info'):
                st.subheader('Dataframe informations:')
                st.text(EA.info())

            if st.sidebar.checkbox('Isnull'):
                st.subheader('Null occurrences')
                st.write(dataFrame.isnull().sum())

            if st.sidebar.checkbox('Unique values and frequency'):
                col = st.sidebar.selectbox('Choose a column for see unique values', EA.columns)
                st.subheader('Unique values and frequency')
                st.write(EA.info2(col))

    except:
        st.error('Upload a CSV file to get started.')


if __name__ == '__main__':
    main()
