from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form['amt']),
            float(request.form['lat']),
            float(request.form['long']),
            float(request.form['city_pop']),
            float(request.form['unix_time']),
            float(request.form['merch_lat']),
            float(request.form['merch_long'])
        ]

        prediction = model.predict([features])[0]

        result = "Fraud ❌" if prediction == 1 else "Legit ✅"

        return render_template("index.html", prediction=result)

    except:
        return render_template("index.html", prediction="Invalid Input ⚠️")

if __name__ == "__main__":
    app.run(debug=True)