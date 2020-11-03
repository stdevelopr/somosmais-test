import json
from app.load_data import dataframe_from_csv, dataframe_from_json, request_csv, request_json, build_df
import pandas as pd

json_model = {
  "type": "laborious",
  "gender": "m",
  "name": {
    "title": "mr",
    "first": "quirilo",
    "last": "nascimento"
  },
  "location": {
    "region": "sul",
    "street": "680 rua treze ",
    "city": "varginha",
    "state": "paraná",
    "postcode": 37260,
    "coordinates": {
      "latitude": "-46.9519",
      "longitude": "-57.4496"
    },
    "timezone": {
      "offset": "+8:00",
      "description": "Beijing, Perth, Singapore, Hong Kong"
    }
  },
  "email": "quirilo.nascimento@example.com",
  "birthday": "1979-01-22T03:35:31Z",
  "registered": "2005-07-01T13:52:48Z",
  "telephoneNumbers": [
    "+556629637520"
  ],
  "mobileNumbers": [
    "+553270684089"
  ],
  "picture": {
    "large": "https://randomuser.me/api/portraits/men/83.jpg",
    "medium": "https://randomuser.me/api/portraits/med/men/83.jpg",
    "thumbnail": "https://randomuser.me/api/portraits/thumb/men/83.jpg"
  },
  "nationality": "BR"
}

def test_request_csv():
  """ Assert the csv resource response """
  resp_csv = request_csv()
  assert resp_csv.status_code == 200

def test_request_json():
  """ Assert the json resource response """
  resp_json = request_json()
  assert resp_json.status_code == 200


def test_dataframe_from_csv():
  """ Assert the every key of the model is present in the csv dataframe columns"""
  df_csv = dataframe_from_csv()

  # assert that the response is a dataframe
  assert isinstance(df_csv, pd.DataFrame)

  # assert that every key is present in the dataframe columns
  for key in json_model:
      assert key in df_csv.columns
      # assert nested keys in the json types
      if isinstance(json_model[key], dict):
        for k1 in json_model[key]:
          assert k1 in df_csv[key].iloc[0]
          if isinstance(json_model[key][k1], dict):
            for k2 in json_model[key][k1]:
              assert k2 in df_csv[key].iloc[0][k1]

def test_dataframe_from_json():
  """ Assert the every key of the model is present in the json dataframe columns"""
  df_json = dataframe_from_json()

  # assert that the response is a dataframe
  assert isinstance(df_json, pd.DataFrame)

  # assert that every key is present in the dataframe columns
  for key in json_model:
      assert key in df_json.columns
      # assert nested keys in the json types
      if isinstance(json_model[key], dict):
        for k1 in json_model[key]:
          assert k1 in df_json[key].iloc[0]
          if isinstance(json_model[key][k1], dict):
            for k2 in json_model[key][k1]:
              assert k2 in df_json[key].iloc[0][k1]

        