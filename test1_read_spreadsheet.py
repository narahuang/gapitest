## This python script is trying to read certain cell from Google spreadsheet
##
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

# json key from Google Developers Console
json_key = json.load(open('canonicaltpeqa-09b0b3ed9933.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

# Open testing spreadsheet, URL: https://docs.google.com/spreadsheets/d/12vX2oVwUaBNUJX-OArExevASE9g--ZWKvHwtJnDGb0g/edit#gid=1084332676
sh = gc.open("googleapitest1")
# Or we can open it by URL
#sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/12vX2oVwUaBNUJX-OArExevASE9g--ZWKvHwtJnDGb0g/edit")

# Select spreadsheet
wks = sh.worksheet("vDT-Stella-Datong")
cid = wks.acell('A29').value
print cid
