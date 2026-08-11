from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ML Model Application is Running"

@app.route("/predict")
def predict():
    return "Prediction: Class 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
