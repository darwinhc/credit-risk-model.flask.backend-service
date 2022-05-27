from flask import Flask, request, abort

from src.model import RiskModel

app = Flask(__name__)
model = RiskModel()


@app.route("/", methods=["POST", "OPTIONS"])
def prediction():
    try:
        return {"prediction": model.predict(request.json)}
    except (ValueError, TypeError):
        abort(400)
