import math
from math import dist
import copy

data = []
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

def leaveOneOutCrossVal(data, finalSelection, x):
    accuracy=0;
    correct = 0;
    for i in range(len(data)): #Classifying i
        nearestDistance = float('inf')
        classI = math.trunc(float(data[i][0]));
        IFeatures=[];
        if(len(finalSelection)!=0): 
            for j in range(len(finalSelection)):
                IFeatures.append(float(data[i][finalSelection[j]]))
        IFeatures.append(float(data[i][x]))
        for k in range(len(data)):
            if i != k:
                classK = math.trunc(float(data[k][0]));
                KFeatures=[];
                if(len(finalSelection)!=0): 
                    for l in range(len(finalSelection)):
                        KFeatures.append(float(data[k][finalSelection[l]]))
                KFeatures.append(float(data[k][x]))
                distance = dist(IFeatures, KFeatures)
                if distance < nearestDistance:
                    nearestDistance=distance
                    nearestLabel = classK
        if classI == nearestLabel:
            correct+=1
    accuracy = correct/len(data)
    return accuracy

def forwardSelection():
    warning = 0
    finalSelection = []
    bestSelection = []
    finalAcc = 0
    print("Beginning Search.")
    for i in range(1, len(data[0]), 1):
        bestAcc = 0;
        bestFeat = 0;
        print("On level " + str(i) + " of the search tree")
        for j in range(1, len(data[0]), 1): #iterate through the features
            if j in bestSelection:
                continue;
            else:
                testAcc = leaveOneOutCrossVal(data, bestSelection, j)
                print("\tUsing feature(s) " + printFeature(bestSelection) + " with {" + str(j) + "} accuracy is " + str(round(testAcc*100,2)) +"%")
                if testAcc > bestAcc:
                    bestAcc = testAcc
                    bestFeat = j
        if warning == 0 and bestAcc < finalAcc:
            warning = 1;
            print("(WARNING: Accuracy has decreased! Continuing search in case of local maxima)")
        elif bestAcc > finalAcc:
            finalAcc = bestAcc
            finalSelection.append(bestFeat)
        
        bestSelection.append(bestFeat);
        print("On level " + str(i) + ", feature set " + printFeature(bestSelection) + " was best, accuracy is "+str(round(bestAcc*100,2))+ "%\n")
    print("Finished search!!! The best feature subset is " + printFeature(finalSelection) + ", which has an accuracy of " + str(round(finalAcc*100,2)) + "%")
    
    return;

def backwardElimination():
    warning = 0
    finalSelection = []
    removedFeature = []
    bestSelection = []
    for i in range(1, len(data[0]), 1):
        bestSelection.append(i)
    finalAcc = 0
    print("Beginning Search.")
    for i in range(1, len(data[0]), 1):
        bestAcc = 0;
        worstAcc=100;
        bestFeat = 0;
        worstFeat = 0
        print("On level " + str(i) + " of the search tree")
        for j in range(1, len(data[0]), 1): #iterate through the features
            if 0:
                continue;
            else:
                # print("before", bestSelection)
                for q in range(len(removedFeature)):
                    if removedFeature[q] in bestSelection:
                        bestSelection.remove(removedFeature[q])
                temp = copy.deepcopy(bestSelection)
                # print("after", bestSelection)
                # print("after", temp)
                if j in removedFeature:
                    continue;
                temp.remove(j)
                testAcc = leaveOneOutCrossVal(data, temp, j)
                print("\tUsing feature(s) " + printFeature(temp) + " with {" + str(j) + "} accuracy is " + str(round(testAcc*100,2)) +"%")
                if testAcc > bestAcc:
                    bestAcc = testAcc
                    bestFeat = j
                if testAcc < worstAcc:
                    worstAcc = testAcc
                    worstFeat = j
        if warning == 0 and bestAcc < finalAcc:
            warning = 1;
            print("(WARNING: Accuracy has decreased! Continuing search in case of local maxima)")
        elif bestAcc > finalAcc:
            finalAcc = bestAcc
            finalSelection.append(bestFeat)
        
        # bestSelection.append(bestFeat);
        removedFeature.append(worstFeat)
        print(removedFeature)
        print("On level " + str(i) + ", feature set " + printFeature(bestSelection) + " was best, accuracy is "+str(round(bestAcc*100,2))+ "%\n")
    print("Finished search!!! The best feature subset is " + printFeature(finalSelection) + ", which has an accuracy of " + str(round(finalAcc*100,2)) + "%")
    
    return;

#main program that runs
def main():
    print("Welcome to the Feature Selection Algorithm");
    # print("Choose the file to test:")
    # fullPath = input("File Input: ");
    fullPath = '/Users/cindyho/Desktop/CS170/cs170_project2/CS170_Small_Data__1.txt' 
    # fullPath = '/Users/cindyho/Desktop/CS170/cs170_project2/CS170_Large_Data__72.txt'
    
    with open(fullPath, 'r') as file:
        for line in file:
            test = line.split()
            data.append(test)
    
    print("\nThis dataset has " + str(len(data[0])-1) + " features (not including the class attribute), with " + str(len(data)) + " instances.\n")

    print("Type the number of the algorithm you want to run:\n1. Forward Selection\n2. Backward Elimination")
    alg_input = 2#int(input("Algorithm Input: "))

    if alg_input == 1:
        print("Forward Selection Chosen.\n")
        forwardSelection();
    else:
        print("Backward Elimination Chosen.\n")
        backwardElimination();

main();