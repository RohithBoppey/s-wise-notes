# reading the csv
from csv import reader
import math
from random import shuffle


def readCSVfile(filename):
    csvData = list()
    with open(filename, 'r') as file:
        csvReader = reader(file)

        for row in csvReader:
            if not row:
                continue
            csvData.append(row)

    return csvData


def convertToFloat(rowData, col):
    for row in rowData:
        row[col] = float(row[col].strip())


filename = 'iris.csv'
csvData = readCSVfile(filename)

for i in range(len(csvData[0])-1):
    # column wise conversion
    convertToFloat(csvData, i)

for row in range(len(csvData)):

    if csvData[row][4] == "Iris-setosa":
        csvData[row][4] = 1

    elif csvData[row][4] == "Iris-versicolor":
        csvData[row][4] = 2

    else:
        csvData[row][4] = 3

shuffle(csvData)

# print(csvData)

training_set = []
testing_set = []

for i in range(120):
    training_set.append(csvData[i])

for i in range(120,150):
    testing_set.append([csvData[i][0], csvData[i][1],
                       csvData[i][2], csvData[i][3]])

# print(training_set)
# print('\n')
# print(testing_set)


def findEuclidianDistance(x1, x2, x3, x4, y1, y2, y3, y4):
    return math.sqrt(pow(x1-y1, 2) + pow(x2-y2, 2) + pow(x3-y3, 2) + pow(x4-y4, 2))

# print(findEuclidianDistance(3,4,0,0))

knn_1 = []
knn_3 = []
for i in range(len(testing_set)):
    euclidian_distance = []
    for j in range(len(training_set)):
        euclidian_distance.append([findEuclidianDistance(testing_set[i][0], testing_set[i][1], testing_set[i][2],
                                  testing_set[i][3], training_set[j][0], training_set[j][1], training_set[j][2], training_set[j][3]),j])
    euclidian_distance.sort(key = lambda num:num[0])

    knn_1.append(training_set[euclidian_distance[0][1]][4])

    arr = [0]*3

    for i in range(3):
        arr[training_set[euclidian_distance[i][1]][4]-1] += 1
    
    knn_3.append(arr.index(max(arr))+1)
# print(euclidian_distance)
# print(len(euclidian_distance))
# print(knn_1)

accuracy = 0

for i in range(len(knn_1)):
    if(knn_1[i] == csvData[i+120][4]):
        accuracy = accuracy + 1
accuracy = accuracy*100/30
print(accuracy)

accuracy = 0
print(knn_3)
for i in range(len(knn_3)):
    if(knn_3[i] == csvData[i+120][4]):
        accuracy = accuracy + 1
accuracy = accuracy*100/30
print(accuracy)



