from flask import current_app, Blueprint, jsonify, request
from app import df
from app.utils import slice_dataframe
import json

clients_bp = Blueprint('clients', __name__, url_prefix='/clients')

def filter_region(df, region):
    if region:
        return df[df['location'].apply(lambda x: x['region']==region)]
    else:
        return df

def filter_type(df, client_type):
    if client_type:
        return df[df['type'] == client_type]
    else:
        return df

@clients_bp.route("/")
def index():
    """ Return a paginated json with users satisfying a query string filtering criteria"""
    region = request.args.get('region')
    client_type = request.args.get('type')
    try:
        pageSize = int(request.args.get('pageSize'))
        pageNumber = int(request.args.get('pageNumber'))
    except:
        pageSize = None
        pageNumber = None

    # filter criterias
    dc = df.pipe(filter_region, region=region).pipe(filter_type, client_type=client_type)

    # count after filter
    totalCount = len(dc.index)

    # apply pagination and parse to json
    if pageSize and pageNumber:
        ds = slice_dataframe(dc, pageSize=pageSize, pageNumber=pageNumber)
    else:
        ds = dc

    result_json = ds.to_json(orient="records")
    parsed_json = json.loads(result_json)
    resp = {
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "totalCount": totalCount,
        "users": parsed_json
    }
    return jsonify(resp)