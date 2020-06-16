import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def mushroomSetup():
    @st.cache(persist=True)
    def load_data():
        data = pd.read_csv("./data/mushrooms.csv")
        labelencoder = LabelEncoder()
        for col in data.columns:
            data[col] = labelencoder.fit_transform(data[col])
        return data

    @st.cache(persist=True)
    def split(df):
        y = df.type
        X = df.drop(columns=['type'])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        return X_train, X_test, y_train, y_test

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

    df = load_data()
    class_names = ['edible', 'poisonous']
    X_train, X_test, y_train, y_test = split(df)
    st.sidebar.subheader("Choose Classifier")
    classifier = st.sidebar.selectbox("",
                                      ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

    if st.sidebar.checkbox("Feature Scaling", False):
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

    if st.checkbox("Display the raw data", False):
        st.subheader("Mushroom DataSet (8124, 23) used for classification problem")
        st.write(df)
        st.markdown(
            "This [data set](https://archive.ics.uci.edu/ml/datasets/Mushroom) includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms "
            "in the Agaricus and Lepiota Family (pp. 500-525). Each species is identified as definitely edible, definitely poisonous, "
            "or of unknown edibility and not recommended. This latter class was combined with the poisonous one.")

    st.subheader("Customize your metric:")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select Type of the Plot", ["Histogram", "box-chart", "kernel density estimation"])
    selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)
    if st.button("Plot a metric"):
        try:
            if type_of_plot == 'Histogram':
                type_of_plot = "hist"
            if type_of_plot == 'box-chart':
                type_of_plot = "box"
            if type_of_plot == "kernel density estimation":
                type_of_plot = 'kde'
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()
        except:
            st.error("choose one column at least!")

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
        bootstrap = st.sidebar.radio("Bootstrap samples when building trees", ('True', 'False'), key='bootstrap')
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
