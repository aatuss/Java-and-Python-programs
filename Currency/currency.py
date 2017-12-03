from sys import argv
def loadCurrencies(fileName):
    data = []
    fileEncoding = "UTF-8"
    with open(fileName, "r", encoding=fileEncoding) as infile:
        for line in infile:
            data.append(line)

    currencies = {}
    for stuff in data:
        pieces = stuff.split("\t")
        currencies[pieces[0]] = Currency(pieces[0],pieces[1],pieces[3])

    return currencies


class Currency:

    def __init__(self, name, fullName, euroRate):
        self.name = name
        self.fullName = fullName
        self.euroRate = float(euroRate)

if __name__ == '__main__':



    data = []
    fileEncoding = "UTF-8"
    with open(argv[1], "r", encoding=fileEncoding) as infile:
        for line in infile:
            data.append(line)

    countries = []
    for stuff in data:
        pieces = stuff.split("\t")
        countries.append(pieces[1])
        countries.sort()
    for j in countries:
        print(j)




