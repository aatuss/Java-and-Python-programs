import json
from sys import argv
import time as dt
import urllib.request
import zipfile

data=[]
webpage = "http://data.itsfactory.fi/journeys/api/1/vehicle-activity"
count = 0
i = 0
while i < int(argv[3]):
    websource = urllib.request.urlopen(webpage)
    jsonData = json.loads(websource.read().decode())
    dt.sleep(int(argv[2]))
    i = i + int(argv[2])
    for key in jsonData:
        count = count + 1
        if count >= 3:
            value = jsonData[key]
            data.append(value)

with open(argv[1], "w", encoding="UTF-8") as outfile:
    json.dump(data, outfile, indent=2)

with zipfile.ZipFile ("busdata.zip","w") as myzip:
    myzip.write(argv[1])