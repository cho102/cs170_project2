import math
from math import dist

data = [] #separated by features
features = 0 #total features (columns)
instances = [] #total rows
#HELPER FUNCTION
def printFeature(set):
    final = "{"
    for i in range(len(set)):
        final += str(set[i])
        final += ", "
    if(len(set)!=0):
        final = final[:-1]
        final = final[:-1]
    final +="}"
    return final

def getFeatures(dt, currFt, newFt):
    temp = []
    if(len(currFt) != 0):
        for i in range(len(currFt)):
            temp.append(float(dt[currFt[i]]))
    temp.append(dt[newFt])
    print(temp)
    float(temp[0])
    return temp;

#TODO: FIX PARAMETERS
def leaveOneOutCrossVal(dataset, currentFeatures, newFeature):
    correctClass = 0
    currentFeatures.append(newFeature)
    print(currentFeatures)
    nearest_distance = float('inf');
    nearest_location = float('inf');
    # for i in range(len(dataset)):
    #     classI = math.trunc(float(dataset[i][0])); #class for the instance
    #     featureI = getFeatures(dataset, currentFeatures, newFeature)
    #     for j in range(len(dataset[i])):
    #         if i != j:
    #             featureJ = getFeatures(dataset[j], currentFeatures, newFeature)
    #             classJ = math.trunc(float(dataset[j][0]))
    #             # print("Ask if " + str(i+1) + " is nearest neighbor with " + str(j+1))
    #             #TODO: NEED TO PERFORM EUCLIDEAN DISTANCE
    #             # distance = dist(featureI, featureJ)#Euclidean
    #             # if distance < nearest_distance:
    #             #     nearest_distance = distance
    #             #     nearest_location = j
    #             #     nearest_label = classJ
    #     # print("Object " + str(i) + " is in class " + str(classI))
    #     # print("\tIts nearest_neighbor is " + str(nearest_location) + " which is in class " + str(classJ))
    #     if classI == classJ:
    #         correctClass +=1
    # accurateClass = correctClass/len(dataset)
    # return math.trunc(accurateClass);

def forwardSelection():
    warning = 0;
    testSelect = []
    select = []
    testAcc = 0
    realAcc = 0
    print("Beginning Search.")
    for i in range(1, 2, 1):
        print("On level " + str(i) + " of the search tree")
        bestFeat = 0;
        bestAcc = 0;
        for j in range(1, features, 1): #iterate through the features
            if j in select:
                continue;
            else:
                testAcc = leaveOneOutCrossVal(instances, select, j)
                print("\tUsing feature(s) " + printFeature(select) + " with {" + str(j) + "} accuracy is " + str(testAcc) +"%")

                # if testAcc > bestAcc:
                #     bestAcc = testAcc
                #     bestFeat = j
        # if warning == 0 and bestAcc < realAcc:
        #     warning = 1;
        #     print("WARNING: Accuracy has decreased! Continuing search in case of local maxima)")
        # else: #SOMETHING IS WEIRD HERE; NEED TO DOUBLE CHECK
        #     realAcc = bestAcc
        #     select.append(bestFeat)
        # print("On level " + str(i) + ", feature set " + printFeature(select) + " was best, accuracy is " + str(realAcc) +"%\n")
    
    print("Finished search!!! The best feature subset is " + "TODO HERE" + ", which has an accuracy of " + "TODO HERE" + "%")
    return;

def backwardElimination():
    print("Beginning Search.")
    print("Finished search!!! The best feature subset is " + "TODO HERE" + ", which has an accuracy of " + "TODO HERE" + "%")
    return;

#main program that runs
def main():
    global data;
    global features;
    global instances;
    print("Welcome to the Feature Selection Algorithm");
    print("Choose the file to test:")
    #TODO: CHANGE PATH FILE
    # fname = input("File Input: ");
    # path = "/Users/cindyho/Desktop/CS170/cs170_project2/"
    # fullPath = '/Users/cindyho/Desktop/CS170/cs170_project2/CS170_Large_Data__72.txt'
    fullPath = '/Users/cindyho/Desktop/CS170/cs170_project2/CS170_Small_Data__1.txt' #= path+fname;
    f = open(fullPath, 'r')
    #Trying to find total features and instances and creating an array of array of each feature
    with open(fullPath, 'r') as file:
        features = len(file.readline().split())
    for i in range(features):
        data.append([])
    with open(fullPath, 'r') as file:
        for line in file:
            test = line.split()
            instances.append(test)
            for i in range(features):
                data[i].append(float(test[i]))
    
    print("\nThis dataset has " + str(features) + " features (not including the class attribute), with " + str(len(instances)) + " instances.\n")
    # initial = 0;
    # print("Running nearest neighbor with all " + str(features) + " features, using \"leaving-one-out\" evaluation, I get an accuracy of " + str(initial) + "%\n")
    
    # print("Type the number of the algorithm you want to run:\n1. Forward Selection\n2.Backward Elimination")
    alg_input = 1 #int(input("Algorithm Input: "))

    if alg_input == 1:
        print("Forward Selection Chosen.\n")
        forwardSelection();
    # else:
    #     print("Backward Elimination Chosen.\n")
    #     backwardElimination();

    # getFeatures(instances[0], [], 4)
    # print(instances[0])
main();

# def testEuclid():
#     print(dist([1, 0, 0], [0, 1, 0]))
# testEuclid()

