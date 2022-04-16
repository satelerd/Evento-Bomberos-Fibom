# the following is the code to get the data of the firemen that will go to the event
# the data comes from a google sheet and is stored in a json file
# we will need to connnect to the google api to get the sheet data

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "service-fibon-key.json", scope
)

client = gspread.authorize(creds)

sheet = client.open(
    "Formulario Entrada FIBOM (respuestas)"
).sheet1  # Open the spreadhseet

# print the data
data = sheet.get_all_records()
pprint(data)


# -----------------------------------------------------------


# from google.oauth2 import service_account
# import gspread
# import pandas as pd

# # Connect to the google api and get the data
# SPREADSHEET = "Formulario Entrada FIBOM (respuestas)"
# credentials = service_account.Credentials.from_service_account_file(
#     "service-fibon-key.json"
# )
# scoped_credentials = credentials.with_scopes(
#     [
#         "https://docs.google.com/spreadsheets/d/1Cf31bdojIQPdJMj52YToKWM_8CWj0AagUXgJWnMxhQ4/edit?usp=sharing"
#     ]
# )

# gc = gspread.authorize(scoped_credentials)

# workbook = gc.open(SPREADSHEET)
# # Get the first sheet
# sheet = workbook.sheet1

# data = pd.DataFrame(sheet.get_all_records())
# print(data)


# ------------------------------------------


# import google.auth
# from google.oauth2 import service_account


# credentials, project = google.auth.default(
#     scopes=['https://www.googleapis.com/auth/cloud-platform'])


# credentials = service_account.Credentials.from_service_account_file(
#     "service-fibon-key.json"
# )

# scoped_credentials = credentials.with_scopes(
#     ["https://www.googleapis.com/auth/cloud-platform"]
# )


# ------------------------------------------


# from __future__ import print_function
# import gspread
# from oauth2client.client import SignedJwtAssertionCredentials
# import pandas as pd
# import json
#
# # Connect to the google api
# SCOPE = ["https://spreadsheets.google.com/feeds"]
# SECRETS_FILE = (
#     r"C:\Users\satel\OneDrive\code\Evento-Bomberos-Fibom\service-fibon-key.json"
# )
# SPREADSHEET = "Formulario Entrada FIBOM (respuestas)"

# json_key = json.load(open(SECRETS_FILE))
# # Authenticate using the signed key
# credentials = SignedJwtAssertionCredentials(
#     json_key["client_email"], json_key["private_key"], SCOPE
# )

# gc = gspread.authorize(credentials)

# print("The following sheets are available")
# for sheet in gc.openall():
#     print("{} - {}".format(sheet.title, sheet.id))
