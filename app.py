import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
import mushromm
import about
from sklearn.preprocessing import StandardScaler
import UploadFile
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score
from sklearn.preprocessing import LabelEncoder


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
    st.header(" **🍄Are your mushrooms Edible or Poisonous?🍄**")


def uploadFile():
    uploaded_file = st.file_uploader("", type="csv")
    if uploaded_file is not None:
        dataFrame = pd.read_csv(uploaded_file)
        labelencoder = LabelEncoder()
        for col in dataFrame.columns:
            dataFrame[col] = labelencoder.fit_transform(dataFrame[col])

    try:
        uploadedData = UploadFile.FileInfo(dataFrame)
        st.success('Successfully uploaded!')
        st.title('Dataset Information:')
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

        if st.sidebar.checkbox(" Train a Model ", False):
            st.title('Choose an out put to Fit a model')
            outputCol = st.selectbox('', uploadedData.columns)
            colIndex = dataFrame.columns.get_loc(outputCol)
            y = dataFrame.iloc[:, colIndex]
            X = dataFrame.drop(columns=[outputCol])
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

            def plot_metrics(metrics_list):
                if 'Confusion Matrix' in metrics_list:
                    st.subheader("Confusion Matrix")
                    plot_confusion_matrix(model, X_test, y_test, display_labels=class_names)
                    st.pyplot()

                if 'ROC Curve' in metrics_list:
                    st.subheader("ROC Curve")
                    plot_roc_curve(model, X_test, y_test)
                    st.pyplot()

                if 'Precision-Recall Curve' in metrics_list:
                    st.subheader('Precision-Recall Curve')
                    plot_precision_recall_curve(model, X_test, y_test)
                    st.pyplot()

            class_names = ['Case1', 'Case2']
            st.sidebar.subheader("Choose Classifier")
            classifier = st.sidebar.selectbox("",
                                              ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

            if st.sidebar.checkbox("Feature Scaling", False):
                sc = StandardScaler()
                X_train = sc.fit_transform(X_train)
                X_test = sc.transform(X_test)

            if classifier == 'Support Vector Machine (SVM)':
                st.sidebar.subheader("Model Hyperparameters")
                C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_SVM')
                kernel = st.sidebar.radio("Kernel", ("rbf", "linear"), key='kernel', index=1)
                gamma = st.sidebar.radio("Gamma (Kernel Coefficient)", ("scale", "auto"), index=1, key='gamma')

                st.sidebar.subheader("Choose metrics to plot:")
                metrics = st.sidebar.multiselect("",
                                                 ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))
                if st.sidebar.button("Classify", key='classify'):
                    st.subheader("Support Vector Machine (SVM) Results")
                    model = SVC(C=C, kernel=kernel, gamma=gamma)
                    model.fit(X_train, y_train)
                    accuracy = model.score(X_test, y_test)
                    y_pred = model.predict(X_test)
                    st.write("Model accuracy: ", accuracy.round(2))
                    st.write("Model precision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                    st.write("Model recall: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                    plot_metrics(metrics)

            if classifier == 'Logistic Regression':
                st.sidebar.subheader("Model Hyperparameters")
                C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_LR')
                max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, key='max_iter')

                metrics = st.sidebar.multiselect("",
                                                 ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

                if st.sidebar.button("Classify", key='classify'):
                    st.subheader("Logistic Regression Results")
                    model = LogisticRegression(C=C, penalty='l2', max_iter=max_iter)
                    model.fit(X_train, y_train)
                    accuracy = model.score(X_test, y_test)
                    y_pred = model.predict(X_test)
                    st.write("Model accuracy: ", accuracy.round(2))
                    st.write("Model precision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                    st.write("Model recall: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                    plot_metrics(metrics)

            if classifier == 'Random Forest':
                st.sidebar.subheader("Model Hyperparameters")
                n_estimators = st.sidebar.number_input("The number of trees in the forest", 100, 5000, step=10,
                                                       key='n_estimators')
                max_depth = st.sidebar.number_input("The maximum depth of the tree", 1, 20, step=1, key='n_estimators')
                bootstrap = st.sidebar.radio("Bootstrap samples when building trees", ('True', 'False'),
                                             key='bootstrap')
                metrics = st.sidebar.multiselect("",
                                                 ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

                if st.sidebar.button("Classify", key='classify'):
                    st.subheader("Random Forest Results")
                    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=bootstrap,
                                                   n_jobs=-1)
                    model.fit(X_train, y_train)
                    accuracy = model.score(X_test, y_test)
                    y_pred = model.predict(X_test)
                    st.write("Model accuracy: ", accuracy.round(2))
                    st.write("Model precision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                    st.write("Model recall: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                    plot_metrics(metrics)

    except:
        st.error('Upload a CSV file to get started.')


if __name__ == '__main__':
    main()
