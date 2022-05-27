from flask import Flask, request, abort
from flask_cors import CORS

from src.model import RiskModel

app = Flask(__name__)
model = RiskModel()
CORS(app)

@app.route("/", methods=["POST", "OPTIONS"])
def prediction():
    try:
        return {"prediction": model.predict(request.json)}
    except (ValueError, TypeError):
        abort(400)
