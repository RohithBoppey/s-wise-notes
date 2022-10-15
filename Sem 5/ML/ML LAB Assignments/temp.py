'''
    PERSONAL INFO:

    NAME : BOPPEY ROHITH
    ROLL NUMBER : S20200010042

'''

# IMPORTS NEEDED ARE
from random import shuffle
from fileinput import filename
from itertools import count
from csv import reader
import math


# Functions part -----------------------------------------------------
# Read string and convert to float and insert into proper array


def convertStringToFloat(rowData, col):
    for row in rowData:
        row[col] = float(row[col].strip())

# This function returns the arrays read from CSV.


def loadCSVintoData(filename):

    CSV_data = list()

    with open(filename, 'r') as file:
        csv_reader = reader(file)

        for row in csv_reader:

            # If not a rwow, only thrn continue.
            if not row:
                continue

            CSV_data.append(row)

    return CSV_data


# File Reading starts here and filename is "iris.csv"
CSVfileName = 'iris.csv'
CSVData = loadCSVintoData(CSVfileName)


# Convert the data read into float and store

for num in range(len(CSVData[0])-1):

    convertStringToFloat(CSVData, num)

    # once the data is converted, then based on that, give the index accordingly
    # this is the mapping function -> flower to 0,1,2
for row in range(len(CSVData)):

    if CSVData[row][4] == "Iris-setosa":
        CSVData[row][4] = 1

    elif CSVData[row][4] == "Iris-versicolor":
        CSVData[row][4] = 2

    else:
        CSVData[row][4] = 3

# This function shuffles the data in the randomised order

shuffle(CSVData)

# Creating arrays for training and testing purposes

training_set = []
testing_set = []

# Storing results of k = 1 and k = 5

KNN_1_result = []
KNN_3_result = []

#  euclidian distance matrix
eu_dist = []


# Creatina a training set

for i in range(120):
    training_set.append(CSVData[i])

for i in range(120, 150):
    testing_set.append(
        [CSVData[i][0], CSVData[i][1], CSVData[i][2], CSVData[i][3]]
    )

for i in range(len(testing_set)):

    for j in range(len(training_set)):

        eu_dist.append([math.sqrt(pow(testing_set[i][0]-training_set[j][0], 2) + pow(testing_set[i][1]-training_set[j]
                                                                                     [1], 2) + pow(testing_set[i][2]-training_set[j][2], 2) + pow(testing_set[i][3]-training_set[j][3], 2)), j])

    eu_dist.sort(key=lambda num: num[0])

    KNN_1_result.append(training_set[eu_dist[0][1]][4])

    knn_arr = 3*[0]

    for k in range(3):
        knn_arr[training_set[eu_dist[k][1]][4]-1] = 1 + \
            knn_arr[training_set[eu_dist[k][1]][4]-1]

    KNN_3_result.append(knn_arr.index(max(knn_arr)) + 1)

    eu_dist.clear()

KNN1 = 0
KNN3 = 0

for i in range(len(KNN_1_result)):
    if CSVData[120+i][4] == KNN_1_result[i]:
        KNN1 += 1
    if CSVData[120+i][4] == KNN_3_result[i]:
        KNN3 += 1

print("\n\n")
print("K = 1 is having the results as: ", end="")
print(KNN_1_result)
print("K Nearest Neighbours (k = 1) is having accuracy : ",
      (KNN1/len(testing_set))*100)

print("K = 3 is having the results as: ", end="")
print(KNN_3_result)
print("K Nearest Neighbours (k = 3) is having accuracy : ",
      (KNN3/len(testing_set))*100)
print("\n\n")