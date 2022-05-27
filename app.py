from flask import Flask, request

from src.model import RiskModel

app = Flask(__name__)
model = RiskModel()


@app.route("/", methods=["POST"])
def prediction():
    return {"prediction": model.predict(request.json)}
