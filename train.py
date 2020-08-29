import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import re

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("progressio Dani Benet").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

day1 = data[1:20:2]
day2 = data[24:39:2]
day3 = data[43:58:2]
day4 = data[63:76:2]
print(re.findall("X[\d]{1,}kg", str(day2)))
