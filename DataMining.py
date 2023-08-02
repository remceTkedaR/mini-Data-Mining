# Data Mining

# Opening the file to Read
myFile = open('plik1.csv', 'r')

# Read the data from file into a list upper() print to table format

listOfLine = myFile.read()
print(listOfLine)
listLine = listOfLine.split(',')
myData = listLine[0]
myDataSplit = myData.split('-')
year = myDataSplit[0]

print(year)


# range print


