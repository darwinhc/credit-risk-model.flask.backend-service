from flask import Flask, request, abort
from flask_cors import CORS

from src.model import RiskModel

app = Flask(__name__)
model = RiskModel()
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["POST"])
def prediction():
    try:
        return {"prediction": model.predict(request.json)}
    except (ValueError, TypeError):
        abort(400)
