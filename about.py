import streamlit as st


def display_about():
    st.markdown('## About')

    st.markdown('A mushroom data set is used from [**UCI** ](https://archive.ics.uci.edu/ml/datasets/Mushroom) which brings machine learning capabailities in binary classification problem to figure out if the mushroom are edible or poisonous.  ')
    st.markdown('This project does not aim to build the best possible classifier or predict model for just one specific classification algorithm, Instead, I build a web app that allows the users to interactively choose the best fit from the different **classification algorithms:** ')

    st.markdown('![Amm](https://raw.github.com/AmmarSahyoun/ModelHints/blob/master/mushroom.jpg)')

    st.markdown('* Support Vector Machine SVM')
    st.markdown('* Logistic Regression')
    st.markdown('* Random Forest')

    st.markdown(' To figure out  the accuracy, precision and recall values, besides that the user could set own parameters values or even choose which metric to plot between:')
    st.markdown('* Confusion Matrix: that shows true/false positive and negative values.')
    st.markdown('* Precision/Recall curve: that show trade-off precision and recall.')


def display_sidebar():
    st.sidebar.markdown('---')
    st.sidebar.title('Contribute')
    st.sidebar.info('If you like the idea and want to contribute to this application, please feel free to contact me and fork my repo [** github **](https://github.com/AmmarSahyoun/ModelHints)')
    st.sidebar.title('About')
    st.sidebar.info('This machine learning web app has been developed as an AI studying assignment by [** Ammar Sahyoun **](https://www.linkedin.com/in/ammar-sahyoun-2498339a/) using: [Python](https://www.python.org/), \
    and [Streamlit](https://streamlit.io/).')
