from flask import current_app, Blueprint, jsonify
from app import df
import json

clients_bp = Blueprint('clients', __name__, url_prefix='/clients')

@clients_bp.route("/")
def index():
    """ Return all clients """
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return jsonify(parsed)