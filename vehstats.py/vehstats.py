from sys import argv
import csv
from collections import Counter
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

#CSV datafile is in argv[1] and PNG file in argv[2]

fileEncoding = "UTF-8"
#for every car
data = []
#for passenger cars
simplifiedData = []
count = 0
countForSimplified = 0
#Max number of lines in file
max = 0

#for 1nd piechart
#getting car brands from simplifiedData
carBrands = []
#Creating counterlist to get data from top 5 brands
counterList = Counter({})
#2 list to add in data from top 5 brands
top5BrandsNumbs = []
top5BrandsNames = []
#Max - combinerBrandAmount
otherBrandsAmount = ""
combinedBrandAmount = ""

#for 2nd chartpie
allKilometers = []
km1 = []
km2 = []
km3 = []
km4 = []
km5 = []
km6 = []
km7 = []

#for 3rd piechart
ages = []
tempDt = ""
#for datetime objects
timesList = []
age5y = []
age10y = []
age15y = []
age20y = []
age25y = []

#for 4nd chartpie
allco2 = []
co21 = []
co22 = []
co23 = []
co24 = []
co25 = []
co26 = []
co27 = []
co28 = []

#reading csv file
with open(argv[1], encoding="ISO-8859-1") as infile:
    csvrd = csv.reader(infile, delimiter=";")
    for line in csvrd:
        count = count + 1
        if count >= 1:
            data.append(line)

for value in data:
    #Narrowing car types to passenger cars
    if value[0] == "M1":
        simplifiedData.append(value)
    # Narrowing car types to passenger cars
    elif value[0] == "M1G":
        simplifiedData.append(value)


        #for first pie chart
#iterating over simplified data to acces car brand which is located in [24] slot
for item in simplifiedData:
    countForSimplified = countForSimplified + 1
    carBrands.append(item[24])
#amount of lines in file
max = countForSimplified

#Using Counter to get 5 most common car brands
BrandData = Counter(carBrands)
BrandData = BrandData.most_common(5)
#Adding them to dictionary
counterList.update(BrandData)
#iterating over dict and adding keys and values into lists
for key, value in counterList:
    top5BrandsNumbs.append(value)
    top5BrandsNames.append(key)

#To get numbers right in piechart
combinedBrandAmount = top5BrandsNumbs[0] + top5BrandsNumbs[1] + top5BrandsNumbs[2] + top5BrandsNumbs[3] + top5BrandsNumbs[4]
#all combined valued from other car brands that are not in TOP5
otherBrandsAmount = max - combinedBrandAmount



       #for 2nd piechart
for kms in simplifiedData:
    if kms[34] != "":
        allKilometers.append(kms[34])

#convert kilometers to int
allKilometers = [int(i) for i in allKilometers]
#adding all invividual kilometers into lists
for km in allKilometers:
    if km >= 0 and km <= 50000:
        km1.append(km)
    elif km >= 50001 and km <= 100000:
        km2.append(km)
    elif km >= 100000 and km <= 150000:
        km3.append(km)
    elif km >= 150000 and km <= 200000:
        km4.append(km)
    elif km >= 20000 and km <= 250000:
        km5.append(km)
    elif km >= 250000 and km <= 300000:
        km6.append(km)
    else:
        km7.append(km)


           #for 3rd piechart
for age in simplifiedData:
    if age[1] != "":
        ages.append(age[1])
#making datetime objects and adding them to new list
for time in ages:
    tempDt = dt.datetime.strptime(time, "%d.%m.%Y")
    timesList.append(tempDt)

now = dt.datetime.now()
years_ago_5 = now.replace(year=now.year-5)
years_ago_10 = now.replace(year=now.year-10)
years_ago_15 = now.replace(year=now.year-15)
years_ago_20 = now.replace(year=now.year-20)
years_ago_25= now.replace(year=now.year-25)

for val in timesList:
    if val >= years_ago_5:
        age5y.append(val)
    elif val < years_ago_5 and val >= years_ago_10:
        age10y.append(val)
    elif val < years_ago_10 and val >= years_ago_15:
        age15y.append(val)
    elif val < years_ago_15 and val >= years_ago_20:
        age20y.append(val)
    elif val < years_ago_20:
        age25y.append(val)

       #for 4nd piehcart
for co2s in simplifiedData:
    if co2s[33] != "":
        allco2.append(co2s[33])
#to int
allco2 = [int(i) for i in allco2]
#gather every co2/kg amounts into own lists according to their values
for amounts in allco2:
    if amounts <= 100:
        co21.append(amounts)
    elif amounts > 100 and amounts <= 125:
        co22.append(amounts)
    elif amounts > 125 and amounts <= 150:
        co23.append(amounts)
    elif amounts > 150 and amounts <= 175:
        co24.append(amounts)
    elif amounts > 175 and amounts <= 200:
        co25.append(amounts)
    elif amounts > 200 and amounts <= 225:
        co26.append(amounts)
    elif amounts > 225 and amounts <= 250:
        co27.append(amounts)
    else:
        co28.append(amounts)

labels1 = [top5BrandsNames[0], top5BrandsNames[1],top5BrandsNames[2], top5BrandsNames[3], top5BrandsNames[4], "Others"]
sizes1 = [top5BrandsNumbs[0], top5BrandsNumbs[1], top5BrandsNumbs[2], top5BrandsNumbs[3], top5BrandsNumbs[4], otherBrandsAmount]
tot1 = sum(sizes1)/ 100.0
autopct1=lambda x: "%d" % round(x*tot1)
colors1 = ["teal","magenta","red","gray","pink","yellow"]

labels2 = ["0-50k km", "51-100k km","100-150k km", "150-200k km", "200-250k km", "250-300k km", ">300k km"]
sizes2 = [len(km1), len(km2), len(km3), len(km4), len(km5), len(km6),len(km7)]
tot2 = sum(sizes2)/ 100.0
autopct2=lambda x: "%d" % round(x*tot2)
colors2 = ["teal","magenta","red","gray","pink","yellow","lightskyblue"]

labels3 = ["<= 5yrs / only 8 exists", ">5 but <=10yrs",">10 but <= 15yrs", ">15 but <=20yrs", ">20yrs"]
sizes3 = [len(age5y), len(age10y), len(age15y), len(age20y), len(age25y)]
tot3 = sum(sizes3)/ 100.0
autopct3=lambda x: "%d" % round(x*tot3)
colors3 = ["teal","magenta","red","pink","lightskyblue"]

labels4 = ["<100 only / 6 exists", ">100 but <=125",">125 but <=150", ">150 but <=175", ">175 but <=200", ">200 but <=225", ">225 but <=250", ">250"]
sizes4 = [len(co21), len(co22), len(co23), len(co24), len(co25), len(co26),len(co27),len(co28)]
tot4 = sum(sizes4)/ 100.0
autopct4=lambda x: "%d" % round(x*tot4)
colors4 = ["blue","palegreen","coral","gray","pink","yellow","goldenrod","khaki"]

explode4 = (0.4,0.2,0,0,0,0,0,0)
explode3 = (0.1,0,0,0,0)
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.pie(sizes1,colors=colors1,startangle=90,shadow=True,autopct=autopct1)
ax1.set_title("Top5 most used car brands")

ax2.pie(sizes2,colors=colors2,startangle=45,shadow=True,autopct=autopct2)
ax2.set_title("Driven kilometers (0km - > 300k km)")

ax3.pie(sizes3,explode=explode3,colors=colors3,startangle=90,shadow=True,autopct=autopct3)
ax3.set_title("Ages of cars from 0 to more than 20 years")

ax4.pie(sizes4,explode=explode4,colors=colors4,startangle=45,shadow=True,autopct=autopct4)
ax4.set_title("CO2 g/km")

first_legend = ax1.legend(labels1, loc = 2,prop={'size': 7})
second_legend = ax2.legend(labels2, loc = 2,prop={'size': 7})
third_legend = ax3.legend(labels3, loc = 2,prop={'size': 6})
fourth_legend = ax4.legend(labels4, loc = 3,prop={'size': 6})

ax1.axis("equal")
ax2.axis("equal")
ax3.axis("equal")
ax4.axis("equal")
fig.tight_layout()

fig.savefig(argv[2])


