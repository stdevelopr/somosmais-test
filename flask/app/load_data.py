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
    df_json = process_json(pd.DataFrame.from_dict(response.json()['results']))
    return df_json


def process_csv(df):
    """Reestructure a csv dataframe and return a new one with new fields"""
    # print(df.columns)
    # Index(['gender', 'name__title', 'name__first', 'name__last',
    #    'location__street', 'location__city', 'location__state',
    #    'location__postcode', 'location__coordinates__latitude',
    #    'location__coordinates__longitude', 'location__timezone__offset',
    #    'location__timezone__description', 'email', 'dob__date', 'dob__age',
    #    'registered__date', 'registered__age', 'phone', 'cell',
    #    'picture__large', 'picture__medium', 'picture__thumbnail'],
    #   dtype='object')

    obj_list = []
    for k, row in df.iterrows():
        json_obj = asdict(Client(
            type="", 
            gender = row['gender'], 
            name = Name(
                title = row['name__title'], 
                first = row['name__first'], 
                last = row['name__last']
                ), 
            location = Location(
                region = "",
                street = row['location__street'],
                city = row['location__city'],
                state= row['location__state'],
                postcode = row['location__postcode'],
                coordinates = Coordinates(
                    latitude = str(row['location__coordinates__latitude']),
                    longitude = str(row['location__coordinates__longitude'])
                    ),
                timezone= Timezone(
                    offset = row['location__timezone__offset'],
                    description= row['location__timezone__description']
                    )
                ),
            email = row['email'],
            birthday = row['dob__date'],
            registered = row['registered__date'],
            telephoneNumbers = ["",""],
            mobileNumbers = ["",""],
            picture = Picture(
                medium= row['picture__medium'], 
                large=row['picture__large'], 
                thumbnail=row['picture__thumbnail']
                ),
            nationality = ""
            )
        )
        obj_list.append(json_obj)

    new_df = pd.DataFrame.from_dict(obj_list)
    return new_df

def process_json(df):
    """Reestructure a json dataframe and return a new one with new fields"""
    # print(df.columns)
    # Index(['gender', 'name', 'location', 'email', 'dob', 'registered', 'phone',
    #    'cell', 'picture'],
    #   dtype='object')
    obj_list = []
    for k, row in df.iterrows():
        json_obj = asdict(Client(
            type="",
            gender = row['gender'],
            name = Name(
                title = row['name']['title'],
                first = row['name']['first'],
                last = row['name']['first']
                ),
            location = Location(
                region = "",
                street = row['location']['street'],
                city = row['location']['city'],
                state= row['location']['state'],
                postcode = row['location']['postcode'],
                coordinates = Coordinates(
                    latitude = str(row['location']['coordinates']['latitude']), 
                    longitude = str(row['location']['coordinates']['longitude'])
                    ),
                timezone= Timezone(
                    offset = row['location']['timezone']['offset'], 
                    description= row['location']['timezone']['description']
                    ) 
                ),
            email = row['email'],
            birthday = row['dob']['date'],
            registered = row['registered']['date'],
            telephoneNumbers = ["",""],
            mobileNumbers = ["",""],
            picture = Picture(
                medium= row['picture']['medium'],
                large=row['picture']['large'],
                thumbnail=row['picture']['thumbnail']
                ),
            nationality = ""
            )
        )
        obj_list.append(json_obj)

    new_df = pd.DataFrame.from_dict(obj_list)
    return new_df

def build_df():
    df_csv = dataframe_from_csv()
    df_json = dataframe_from_json()
    df = pd.concat([df_csv, df_json])
    return df