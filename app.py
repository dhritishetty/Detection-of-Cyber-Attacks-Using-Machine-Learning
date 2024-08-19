import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.ipynb')

@app.route('/')
def home():
    return render_template('frame.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]

    if int_features[0] == 0:
        f_features = [0, 0, 0] + int_features[1:]
    elif int_features[0] == 1:
        f_features = [1, 0, 0] + int_features[1:]
    elif int_features[0] == 2:
        f_features = [0, 1, 0] + int_features[1:]
    else:
        f_features = [0, 0, 1] + int_features[1:]

    if f_features[6] == 0:
        fn_features = f_features[:6] + [0, 0] + f_features[7:]
    elif f_features[6] == 1:
        fn_features = f_features[:6] + [1, 0] + f_features[7:]
    else:
        fn_features = f_features[:6] + [0, 1] + f_features[7:]

    final_features = [np.array(fn_features)]
    prediction_result = model.predict(final_features)

    if prediction_result == 0:
        output = 'Normal'
    elif prediction_result == 1:
        output = 'DOS'
    elif prediction_result == 2:
        output = 'PROBE'
    elif prediction_result == 3:
        output = 'R2L'
    else:
        output = 'U2R'

    return render_template('frame.html', prediction=output)

@app.route('/results',methods=['GET'])
def results():
    data = request.get_json(force=True)
    predicted_label = model.predict([np.array(list(data.values()))])

    if predicted_label == 0:
        output = 'Normal'
    elif predicted_label == 1:
        output = 'DOS'
    elif predicted_label == 2:
        output = 'PROBE'
    elif predicted_label == 3:
        output = 'R2L'
    else:
        output = 'U2R'

    return jsonify(output)

if __name__ == "__main__":
    app.run()
