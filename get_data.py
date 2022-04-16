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
    "../service-fibon-key.json", scope
)

client = gspread.authorize(creds)

sheet = client.open(
    "Formulario Entrada FIBOM (respuestas)"
).sheet1  # Open the spreadhseet

# print the data
data = sheet.get_all_records()
pprint(data)
