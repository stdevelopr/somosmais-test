from flask import current_app
import pandas as pd
import requests
from io import StringIO
import csv
import json


def dataframe_from_csv():
    """ Return a structured pandas dataframe from a requested csv file"""
    resp_csv = requests.get("https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv")
    s = str(resp_csv.content,'utf-8')
    csv_file = StringIO(s)
    df_csv = process_csv(pd.read_csv(csv_file))
    return df_csv


def process_csv(df):
    """Reestructure a csv dataframe and return a new one with new fields"""
    obj_list = []
    for k, row in df.iterrows():
        json_obj = {
            "type":"",
            "gender":"",
            "name":"",
            "location":"",
            "timezone":"",
            "email":"",
            "birthday":"",
            "registered":"",
            "telephoneNumbers":"",
            "mobileNumbers":"",
            "picture":"",
            "nationality":""
            
        }
        obj_list.append(json_obj)

    new_df = pd.DataFrame.from_dict(obj_list)
    return new_df


def build_df():
    df_csv = dataframe_from_csv()
    return df_csv