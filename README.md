ModelHints https://modelhints.herokuapp.com/

![](/modelHints.gif)


<h4>Choose the best classification model </h4>

-I use Python and Streamlit to build the dashboard.
-I used mushrooms data set from UCI: https://archive.ics.uci.edu/ml/datasets/Mushroom
I choose this data set because it usually used for binary classification tasks to figure out if your mushrooms are edible or poisonous.
-This project does not aim to build the best possible classifier or predict model for just one specific classification algorithm, Instead, I build a web app that allows the users to upload their own CSV files, analyze the data association and interactively tune the hyperparameters of the classifiers: 
1-Support Vector Machine SVM
2-Logistic Regression
3-Random Forest

To figure out:
-Accuracy: How often is the classifier correct.
-precision: How often is it correct to classify (TP,FN)
-recall “sensitivity”: a rate that shows how often does it predict yes
 besides that the user could set own parameters values or even choose which metric to plot between:
-Confusion Matrix: that shows true/false positive and negative values.
-Precision/Recall curve: that show trade-off precision and recall.

<h2>Conclusion</h2>
I figure out that 'Random Forest' model fits out data with the best accuracy value.
Even though experts have determined that is that there is no simple set of rules to determine whether a mushroom is edible or not, it seems like with this algorithm we can get pretty close. because our result based on this dataset.
https://modelhints.herokuapp.com/
