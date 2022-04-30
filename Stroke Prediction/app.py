from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def stroke():
    return render_template('stroke.html')


strokemodel = pickle.load(open('Machine Learning Model/StrokeModel.pickle', 'rb'))

@app.route('/', methods=['POST'])
def strokepred():
    gender = {"Male": 1, "Female" : 0}
    residence = {"Urban" : 1, "Rural": 0}
    smoking_status = {"Unknown" : 0, "Formerly Smoked":1, "Never Smoked":2, "Smokes" : 3}
    work_type = {"Government Job" : 0, "Never Worked" : 1, "Private" : 2, "Self-Employed" : 3, "Children": 4}
    yes_no = {"No": 0, "Yes": 1}
    arr = []
    for ch in "abcdefghij":
        arr.append(request.form[ch])
    arr[0] = gender[arr[0]]
    arr[2] = yes_no[arr[2]]
    arr[3] = yes_no[arr[3]]
    arr[4] = yes_no[arr[4]]
    arr[5] = work_type[arr[5]]
    arr[6] = residence[arr[6]]
    arr[9] = smoking_status[arr[9]]

    arr = np.array(arr)
    arr = np.expand_dims(arr, axis=0)
    pred = strokemodel.predict(arr)
    probs = strokemodel.predict_proba(arr)
    idx = np.argmax(probs)
    confidence = probs.flatten()[idx]
    confidence = round(confidence, 2)
    confidence *= 100
    return render_template('stroke.html', data=pred, confidence=confidence)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
