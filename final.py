import math
from math import dist
import copy
from itertools import combinations
import time

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
        bestFeatCombo = 0;
        worstFeatCombo = 0;
        worstFeat = 0;
        print("On level " + str(i) + " of the search tree")
        temp=[]
        temp += list(combinations(bestSelection, len(data[0])-i))
        for j in range(len(temp)):
            tempJ = list(copy.deepcopy(temp[j]))
            val = tempJ.pop(0)
            testAcc = leaveOneOutCrossVal(data, tempJ, val)
            print("\tUsing feature(s) " + printFeature(temp[j]) + " accuracy is " + str(round(testAcc*100,2)) +"%")
            if testAcc > bestAcc:
                bestAcc = testAcc
                bestFeatCombo = temp[j]
            if testAcc < worstAcc:
                worstAcc = testAcc
                worstFeatCombo = temp[j]
        if warning == 0 and bestAcc < finalAcc:
            warning = 1;
            print("(WARNING: Accuracy has decreased! Continuing search in case of local maxima)")
        elif bestAcc > finalAcc:
            finalAcc = bestAcc
            finalSelection = bestFeatCombo
        if bestFeatCombo != worstFeatCombo:
            difference = list(set(worstFeatCombo).symmetric_difference(bestFeatCombo))
            for q in range(len(difference)):
                if difference[q] in worstFeatCombo:
                    worstFeat = difference[q]
            removedFeature.append(worstFeat)
            bestSelection.remove(worstFeat)
        print("On level " + str(i) + ", feature set " + printFeature(bestFeatCombo) + " was best, accuracy is "+str(round(bestAcc*100,2))+ "%")
        if worstFeat!=0: print("On level " + str(i) + ", feature set with " + str(worstFeat) + " was the worst\n")
        else: print("")
    print("Finished search!!! The best feature subset is " + printFeature(finalSelection) + ", which has an accuracy of " + str(round(finalAcc*100,2)) + "%")
    return;

#main program that runs
def main():
    print("Welcome to the Feature Selection Algorithm");
    print("Choose the file to test:")
    # fullPath = input("File Input: ");
    # fullPath = '/Users/cindyho/Desktop/CS170/cs170_project2/CS170_Small_Data__1.txt' 
    fullPath = '/Users/cindyho/Desktop/CS170/cs170_project2/CS170_Large_Data__72.txt'
    
    with open(fullPath, 'r') as file:
        for line in file:
            test = line.split()
            data.append(test)
    
    print("\nThis dataset has " + str(len(data[0])-1) + " features (not including the class attribute), with " + str(len(data)) + " instances.\n")

    print("Type the number of the algorithm you want to run:\n1. Forward Selection\n2. Backward Elimination")
    alg_input = int(input("Algorithm Input: "))
    start_time=time.time();
    if alg_input == 1:
        print("Forward Selection Chosen.\n")
        forwardSelection();
    else:
        print("Backward Elimination Chosen.\n")
        backwardElimination();
    end_time = time.time() - start_time
    if end_time <60:
        print("Total time elapsed(in seconds): " + str(round(end_time, 1))+ "\n\n")
    else:
        print("Total time elapsed(in minutes): " + str(round(end_time/60, 1))+ "\n\n")
main();