import os
import pandas
import json

script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path)
data_path = os.path.join(folder_path, "data-ualberta.xlsx")
xls = pandas.ExcelFile(data_path)
datafile = pandas.read_excel(data_path, sheet_name="requisites")
datafile.fillna('', inplace=True)
for data in datafile:
    datafile.
data = datafile.to_csv()
f = open("data-uofa-prerequisites.json", "w")
f.write(json.dumps(data))
f.close()
