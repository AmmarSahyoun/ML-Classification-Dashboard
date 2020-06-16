import streamlit as st

def display_about():
    st.markdown('## About')

    st.markdown('The [**UCI mushroom dataset** ](https://archive.ics.uci.edu/ml/datasets/Mushroom) that provides machine learning capabilities is used in binary classification problem to see if the mushroom is edible or poisonous. ')
    st.markdown('This project does not aim to just fit and plot 3-classifiers with the mushroom dataset, **Moreover**, I build a web app that allows the users to upload their own CSV files, analyze the data association and **interactively tune the hyperparameters of the classifiers: ** ')
    st.markdown('1- Support Vector Machine ')
    st.markdown('2- Logistic Regression')
    st.markdown('3- Random Forest')
    st.markdown(' To figure out the **accuracy**, **precision** and **recall** values. Besides that the user could set own parameters values or even choose which metric to plot between:')
    st.markdown('* Confusion Matrix: that shows true/false positive and negative values.')
    st.markdown('* Roc_curve: a graph that summarizes the classifier performance.')
    st.markdown('* Precision/Recall : that show trade-off precision and recall.')

def display_contribute():
    st.sidebar.markdown('---')
    st.sidebar.title('About')
    st.sidebar.info('Model Hints web app **version 0.0.1** has been developed as an AI Collage assignment by [** Ammar Sahyoun **](https://www.linkedin.com/in/ammar-sahyoun-2498339a/) using: [Python](https://www.python.org/), \
        and [Streamlit](https://streamlit.io/).')
    st.sidebar.title('Contribute')
    st.sidebar.info('If you like the idea and want to contribute to this application, please feel free to contact me and fork my repo [** github **](https://github.com/AmmarSahyoun/ModelHints)')
