from app.utils import client_type_from_coordinates, gender_type, \
                        process_tel, generate_telephone_list, get_region, strip_accents, \
                        get_country_code, slice_dataframe
import pytest
import pandas as pd

def test_client_type_from_coordinates():
    """ Assert the client type according to their coordinates"""
    assert client_type_from_coordinates(long=-10, lat=-40) == 'special'
    assert client_type_from_coordinates(long=-10, lat=-30) == 'laborious'
    assert client_type_from_coordinates(long=-20, lat=-50) == 'special'
    assert client_type_from_coordinates(long=-20, lat=-30) == 'laborious'
    assert client_type_from_coordinates(long=-30, lat=-50) == 'normal'
    assert client_type_from_coordinates(long=-30, lat=-60) == 'laborious'

def test_gender():
    """ Assert the gender type representation """
    assert gender_type("female") == "F"
    assert gender_type("Male") == "M"
    with pytest.raises(Exception):
        gender_type("Unknow")

def test_process_telephone():
    """ Assert that the processed number is in correct format """
    tel = process_tel("BR", "(86) 8370-9831")
    assert tel == "+558683709831"

def test_generate_telephone_list():
    tel_list = generate_telephone_list("BR", "(86) 8370-9831,(11) 9878-1534")
    assert tel_list == ["+558683709831", "+551198781534"]


def test_country_code():
    """ Assert the country code, default BR +55 """
    assert get_country_code() == "+55"

def test_strip_acents():
    assert strip_accents("amapá") == "amapa"
    assert strip_accents("são paulo") == "sao paulo"

def test_region():
    assert get_region('amapá') == 'norte'
    assert get_region('São Paulo') == 'sudeste'

def test_slice_dataframe():
    d = {'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}
    df = pd.DataFrame(data=d)
    assert list(slice_dataframe(df, pageSize=1, pageNumber=1)['col1']) == [1]
    assert list(slice_dataframe(df, pageSize=2, pageNumber=1)['col1']) == [1, 2]
    assert list(slice_dataframe(df, pageSize=2, pageNumber=2)['col1']) == [3, 4]
    assert list(slice_dataframe(df, pageSize=4, pageNumber=2)['col1']) == [5, 6, 7, 8]
    assert list(slice_dataframe(df, pageSize=2, pageNumber=3)['col1']) == [5, 6]
    assert list(slice_dataframe(df, pageSize=5, pageNumber=4)['col1']) == [16]