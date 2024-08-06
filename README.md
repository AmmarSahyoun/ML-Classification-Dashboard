# ML-Classification-Dashboard

## Overview
This repository contains a Streamlit-based application for binary classification problem. Users can upload their CSV data, explore data associations, tune hyperparameters for **SVM**, **Logistic Regression**, and **Random Forest classifiers**, and evaluate model performance using metrics like **accuracy**, **precision**, **recall**, and **confusion matrices**. 

## Features
* **Data Upload:** Supports CSV file uploads for classification tasks.
* **Exploratory Data Analysis (EDA):** Provides basic data exploration capabilities.
* **Model Selection:** Offers SVM, Logistic Regression, and Random Forest classifiers.
* **Hyperparameter Tuning:** Allows interactive adjustment of model hyperparameters.
* **Model Evaluation:** Calculates accuracy, precision, recall, and confusion matrices.
* **Visualization:** Generates precision-recall curves for model comparison.

### Clone the repository:
   ```bash
   git clone https://github.com/AmmarSahyoun/ML-Classification-Dashboard.git
   ```




![](/modelHints.gif)


<h2>Own experiment</h4>


In this project, I utilized the well-known UCI Machine Learning Repository's mushroom dataset (https://archive.ics.uci.edu/dataset/73/mushroom) for a binary classification task to distinguish between edible and poisonous mushrooms.

The focus of this project wasn't just on achieving the absolute best possible classifier or solely predicting using a single classification algorithm. But also, I aimed to create a web application that empowers users to:

- Upload their own CSV data.
- Analyze data associations within the uploaded data.
- Interactively tune hyperparameters for three machine learning classifiers:
    1. Support Vector Machine (SVM)
    2. Logistic Regression
    3. Random Forest

Through this interactive exploration, users can gain insights into model performance using various metrics:

- **Accuracy:** How often is the classifier correct.
- **precision:** How often is it correct to classify (TP,FN)
- **recall “sensitivity”:** a rate that shows how often does it predict yes
 besides that the user could set own parameters values or even choose which metric to plot between:
- **Confusion Matrix:** that shows true/false positive and negative values.
- **Precision/Recall** curve: that show trade-off precision and recall.

<h3>Conclusion</h3>
I figure out that 'Random Forest' model fits out data with the best accuracy value.
Even though experts have determined that is that there is no simple set of rules to determine whether a mushroom is edible or not, it seems like with this algorithm we can get pretty close. because our result based on this dataset.

The dashboard deployed in herokuapp benefiting one year free hosting wehere I called it modelHints.
https://modelhints.herokuapp.com/
