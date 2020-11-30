import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
print(exampleReader)
exampleData = list(exampleReader)
print(exampleData)

print()
print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[1][1])
print(exampleData[6][1])