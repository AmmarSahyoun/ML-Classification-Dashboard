import streamlit as st
import pandas as pd
import about
import modelHints
from PIL import Image

def main():
    st.success("# _Model Hints Web App_ `version0.0.1` ")
    st.title("3-Binary Problem Classifier")
    img = Image.open("./templates/mushroom.jpg")
    st.image(img)
    st.header(" **🍄Are your mushrooms edible or poisonous?🍄**")


    menu = ['Model Hints', 'About']
    menuSelection = st.sidebar.radio('', menu, index=1, key=None)
    if menuSelection == 'About':
        about.display_about()
        about.display_contribute()
    if menuSelection == 'Model Hints':
        modelHints.setup()


if __name__ == '__main__':
    main()
