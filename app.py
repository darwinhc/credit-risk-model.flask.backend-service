from flask import Flask, request, abort

from src.model import RiskModel

app = Flask(__name__)
model = RiskModel()


@app.route("/", methods=["POST"])
def prediction():
    try:
        return {"prediction": model.predict(request.json)}
    except (ValueError, TypeError) as err:
        abort(400)
