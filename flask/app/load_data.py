import pandas as pd
import requests
from io import StringIO
import csv
from .model import Client, Name, Location, Coordinates, Timezone, Picture
from dataclasses import asdict


def request_csv():
    """ Make a request to a csv resource and return the file"""
    resp_csv = requests.get("https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv")
    return resp_csv

def request_json():
    """ Make a request to a json resource and return the file"""
    resp_json = requests.get("https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json")
    return resp_json


def dataframe_from_csv():
    """ Return a structured pandas dataframe from a requested csv file"""
    response = request_csv()
    s = str(response.content,'utf-8')
    csv_content = StringIO(s)
    df_csv = process_csv(pd.read_csv(csv_content))
    return df_csv


def dataframe_from_json():
    """ Return a structured pandas dataframe from a requested json file"""
    response = request_json()
    df_json = process_json(pd.DataFrame.from_dict(response.json()))
    return df_json


def process_csv(df):
    """Reestructure a csv dataframe and return a new one with new fields"""
    obj_list = []
    for k, row in df.iterrows():
        json_obj = asdict(Client(
            type="", 
            gender = "", 
            name = Name(
                title = "", 
                first = "", 
                last = ""
                ), 
            location = Location(
                region = "",
                street = "",
                city = "",
                state= "",
                postcode = 0,
                coordinates = Coordinates(
                    latitude = 0.0,
                    longitude = 0.0
                    ),
                timezone= Timezone(
                    offset = "",
                    description= ""
                    )
                ),
            email = "",
            birthday = "",
            registered = "",
            telephoneNumbers = ["",""],
            mobileNumbers = ["",""],
            picture = Picture(
                medium= "", 
                large="", 
                thumbnail=""
                ),
            nationality = ""
            )
        )
        obj_list.append(json_obj)

    new_df = pd.DataFrame.from_dict(obj_list)
    return new_df

def process_json(df):
    """Reestructure a json dataframe and return a new one with new fields"""
    obj_list = []
    for k, row in df.iterrows():
        json_obj = asdict(Client(
            type="",
            gender = "",
            name = Name(
                title = "",
                first = "",
                last = ""
                ),
            location = Location(
                region = "",
                street = "",
                city = "",
                state= "",
                postcode = 0,
                coordinates = Coordinates(
                    latitude = 0.0, 
                    longitude = 0.0
                    ),
                timezone= Timezone(
                    offset = "", 
                    description= ""
                    ) 
                ),
            email = "",
            birthday = "",
            registered = "",
            telephoneNumbers = ["",""],
            mobileNumbers = ["",""],
            picture = Picture(
                medium= "",
                large="",
                thumbnail=""
                ),
            nationality = ""
            )
        )
        obj_list.append(json_obj)

    new_df = pd.DataFrame.from_dict(obj_list)
    return new_df

def build_df():
    df_csv = dataframe_from_csv()
    return df_csv