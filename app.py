import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score


def main():
    st.title("Model Hints Web App")
    st.title("Binary Problem Classification")
    st.sidebar.title("ModelHints WebApp")
    st.markdown("Q: 🍄Are your mushrooms edible or poisonous?🍄")
    st.sidebar.markdown("Are your mushrooms edible or poisonous? 🍄")

    @st.cache(persist=True)
    def load_data():
        data = pd.read_csv("mushrooms.csv")
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

    df = load_data()
    X_train, X_test, y_train, y_test = split(df)

    if st.sidebar.checkbox("Show raw data", False):
        st.subheader("Mushroom DataSet (8124, 23) used for classification problem")
        st.write(df)


if __name__ == '__main__':
    main()
