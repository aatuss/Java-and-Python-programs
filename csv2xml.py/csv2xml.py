from sys import argv
import csv
from xml.etree.ElementTree import ElementTree as ET, Element, SubElement
from bs4 import BeautifulSoup

fileEncoding = "UTF-8"
countForLines = 0
data = []
with open(argv[1], encoding=fileEncoding) as infile:
    csvrd = csv.reader(infile, delimiter=";")
    for line in csvrd:
        # for skipping first 5 lines which are not wanted
        countForLines = countForLines + 1
        if countForLines >= 5:
            data.append(line)

#Adding root element before loop so every other element will be added inside it
root = Element("populationdata")
for item in data:
    #creating elements. Municipality will be added to root element as a subElement
    mc = SubElement(root, "municipality")
    #Rest of the elements will be added to Municipality as subElements
    name = SubElement(mc, "name")
    year = SubElement(mc, "year")
    total = SubElement(mc, "total")
    males = SubElement(mc, "males")
    females = SubElement(mc, "females")
    name.text = item[0]
    year.text = item[1]
    total.text = item[2]
    males.text = item[3]
    females.text = item[4]
    #Forming element tree
    tree = ET(root)
#writing element tree into XML file
    tree.write(argv[2], encoding="utf-8", xml_declaration=True, method="xml")

#Opening XML file as "soup"
bs = BeautifulSoup(open(argv[2]), "xml")
#Formatting the XML using soup to get pretty printed format
with open(argv[2],"w") as out:
    out.write(bs.prettify())


