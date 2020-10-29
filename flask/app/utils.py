#generic functions to manipulate and classify data

import re
import unicodedata


def client_type_from_coordinates(lat: float, long:float):
    """ Return the client type according to their coordinates """
    if ((-15.411580 <= long <= -2.196998 and -46.361899 <= lat <= -34.276938) 
        or (-23.966413 <= long <= -19.766959 and -52.997614 <= lat <= -44.428305)):
        return "special"
    elif (-34.016466 <= long <= -26.155681 and -54.777426 <= lat <= -46.603598):
        return "normal"
    else:
        return "laborious"

def gender_type(gender:str):
    """ Return a gender classification type """
    if gender.lower() == "female":
        return "F"
    elif gender.lower() == "male":
        return "M"
    else:
        raise Exception("Unknow gender", gender)

def generate_telephone_list(country: str, telephones: str):
    """ Return a list from a telephone string """
    tel_list = []
    tel_split = telephones.split(",")
    for tel in tel_split:
        tel_proc = process_tel(country, tel)
        tel_list.append(tel_proc)

    return tel_list

def process_tel(country: str, tel: str):
    """ Return a new processed telephone number """
    code = get_country_code(country)
    pattern = re.compile(r'\d+')
    number = code+"".join(re.findall(pattern, tel))

    return number

def get_nationality():
    """ TODO Return a nationality based on some parameter """
    return "BR"

def get_country_code(country: str = "BR"):
    """ Return the code of the country """
    country_codes = {
        "BR": "+55"
    }

    code = country_codes.get(country, "???")

    return code


def get_region(state: str):
    """ Return the region according to the state """
    regions = {
        'acre': 'norte',
        'alagoas': 'nordeste',
        'amapa' : 'norte',
        'amazonas': 'norte',
        'bahia' : 'nordeste',
        'ceara': 'nordeste',
        'distrito federal': 'centro-oeste',
        'espirito santo': 'sudeste',
        'goias' : 'centro-oeste',
        'maranhao' : 'nordeste',
        'mato grosso' : 'centro-oeste',
        'mato grosso do sul' : 'centro-oeste',
        'minas gerais' : 'sudeste',
        'para' : 'norte',
        'paraiba' : 'nordeste',
        'parana' : 'sul',
        'pernambuco' : 'nordeste',
        'piaui' : 'nordeste',
        'rio de janeiro' : 'sudeste',
        'rio grande do norte' : 'nordeste',
        'rio grande do sul' : 'sul',
        'rondonia' : 'norte',
        'roraima' : 'norte',
        'santa catarina' : 'sul',
        'sao paulo' : 'sudeste',
        'sergipe' : 'nordeste',
        'tocantins': 'norte'
    }

    s= strip_accents(state.lower())

    return regions[s]

def strip_accents(s):
    """ Remove accents from a string """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


def slice_dataframe(df, pageSize, pageNumber):
    """ Slice a dataframe according to pagesize and pageNumber """
    pageSize = pageSize
    pageNumber = pageNumber
    start_index = pageSize*(pageNumber - 1)
    end_index = start_index + pageSize
    ds = df[start_index : end_index]
    return ds



