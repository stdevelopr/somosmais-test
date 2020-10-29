from flask import current_app, Blueprint, jsonify
from app import df
from app.utils import slice_dataframe
import json

clients_bp = Blueprint('clients', __name__, url_prefix='/clients')

@clients_bp.route("/")
def index():
    """ Return all clients """

    # pagination parameters
    pageSize = 10
    pageNumber = 1

    # filter criterias
    region = df['location'].apply(lambda x: x['region']=='sul')
    type_ = df['type']=='laborious'
    dc = df.loc[region & type_]

    # count after filter
    totalCount = len(dc.index)

    # apply pagination and parse to json
    ds = slice_dataframe(dc, pageSize=pageSize, pageNumber=pageNumber)
    result_json = ds.to_json(orient="records")
    parsed_json = json.loads(result_json)
    resp = {
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "totalCount": totalCount,
        "users": parsed_json
    }
    return jsonify(resp)