from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

# pkl_file = open('/model.pkl', 'rb')
# model = pickle.load(pkl_file)
# pkl_file.close()


# objects = []
# with (open("myfile", "rb")) as openfile:
#     while True:
#         try:
#             objects.append(pickle.load(openfile))
#         except EOFError:
#             break

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('index.html',
                               pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),
                               bhai="kuch karna hain iska ab?")
    else:
        return render_template('index.html',
                               pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),
                               bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True)
