'''
Assigment 2 - data retriving
'''
import pandas
import numpy
import csv
import os

dataFile = "nesarc_pds.csv" 
maxRaws = 50

############################################################
###################### Util functions ######################
############################################################

'''
Crates a sampled csv file, as the original data set is large to process
'''
def sampleRows():

    myfile = open("tmp_nesarc_pds.csv", 'w')
    writer = csv.writer(myfile)

    with open('nesarc_pds.csv') as csvfile:
        i = 0
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if maxRaws <= i:
                break
            i += 1
            writer.writerow(row)

def sampleColumn():
    myfile = open("column_data.csv", 'w')
    writer = csv.writer(myfile)

    with open('nesarc_pds.csv') as csvfile:
        i = 0
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if maxRaws <= i:
                break
            i += 1
            writer.writerow([row[496]])

############################################################
##################### In use functions #####################
############################################################

def updatingSmokingData(data):
    #USUAL FREQUENCY WHEN SMOKED CIGARETTES
    data['S3AQ3B1'] = data['S3AQ3B1'].convert_objects(convert_numeric=True)

def updateIndividualDepression(data):
    #DURATION (WEEKS) OF ONLY/LONGEST EPISODE (BASED ON S4AQ9E IF ONLY 1 EPISODE)
    data['S4AQ9DR'] = data['S4AQ9DR'].convert_objects(convert_numeric=True)

def updateFamilyDepression(data):
    #BLOOD/NATURAL FATHER EVER DEPRESSED
    data['S4BQ1'] = data['S4BQ1'].convert_objects(convert_numeric=True)
    #BLOOD/NATURAL MOTHER EVER DEPRESSED
    data['S4BQ2'] = data['S4BQ2'].convert_objects(convert_numeric=True)
    #ANY FULL BROTHERS EVER DEPRESSED
    data['S4BQ3C'] = data['S4BQ3C'].convert_objects(convert_numeric=True)
    #ANY FULL SISTERS EVER DEPRESSED
    data['S4BQ4C'] = data['S4BQ4C'].convert_objects(convert_numeric=True)
    #ANY NATURAL SONS EVER DEPRESSED
    data['S4BQ5C'] = data['S4BQ5C'].convert_objects(convert_numeric=True)
    #ANY NATURAL DAUGHTERS EVER DEPRESSED
    data['S4BQ6C'] = data['S4BQ6C'].convert_objects(convert_numeric=True)
    #NATURAL GRANDFATHER ON YOUR FATHER'S SIDE EVER DEPRESSED
    data['S4BQ11'] = data['S4BQ11'].convert_objects(convert_numeric=True)
    #NATURAL GRANDMOTHER ON YOUR FATHER'S SIDE EVER DEPRESSED
    data['S4BQ12'] = data['S4BQ12'].convert_objects(convert_numeric=True)
    #NATURAL GRANDFATHER ON YOUR MOTHER'S SIDE EVER DEPRESSED
    data['S4BQ13'] = data['S4BQ13'].convert_objects(convert_numeric=True)
    #NATURAL GRANDMOTHER ON YOUR MOTHER'S SIDE EVER DEPRESSED
    data['S4BQ14'] = data['S4BQ14'].convert_objects(convert_numeric=True)

def printFormattedData(data, header, attributeName):
    print('Count: ' + header)
    c1 = data[attributeName].value_counts(sort=False)
    print (str(c1)  + "\n")
    print('Percentage: ' + header)
    p1 = data[attributeName].value_counts(sort=False, normalize=True)
    print (str(p1) + '\n*********\n')

def printSmokingdistribution(data):
    printFormattedData(data, "USUAL FREQUENCY WHEN SMOKED CIGARETTES",'S3AQ3B1')

def printIndividualDepression(data):
    printFormattedData(data, "DURATION (WEEKS) OF ONLY/LONGEST EPISODE (BASED ON S4AQ9E IF ONLY 1 EPISODE)", 'S4AQ9DR')
    
def printFamilyDepression(data):
    printFormattedData(data, "BLOOD/NATURAL FATHER EVER DEPRESSED", 'S4BQ1')
    printFormattedData(data, "BLOOD/NATURAL MOTHER EVER DEPRESSED",'S4BQ2')
    printFormattedData(data, "ANY FULL BROTHERS EVER DEPRESSED",'S4BQ3C')
    printFormattedData(data, "ANY FULL SISTERS EVER DEPRESSED", 'S4BQ4C')
    printFormattedData(data, "ANY NATURAL SONS EVER DEPRESSED", 'S4BQ5C')
    printFormattedData(data, "ANY NATURAL DAUGHTERS EVER DEPRESSED",'S4BQ6C')
    printFormattedData(data, "NATURAL GRANDFATHER ON YOUR FATHER'S SIDE EVER DEPRESSED",'S4BQ11')
    printFormattedData(data, "NATURAL GRANDMOTHER ON YOUR FATHER'S SIDE EVER DEPRESSED",'S4BQ12')
    printFormattedData(data, "NATURAL GRANDFATHER ON YOUR MOTHER'S SIDE EVER DEPRESSED",'S4BQ13')
    printFormattedData(data, "NATURAL GRANDMOTHER ON YOUR MOTHER'S SIDE EVER DEPRESSED",'S4BQ14')

def printDepressedAndSmoking(data):
    everyDaySmoker = data[data['S3AQ3B1'] == 1]
    printFormattedData(everyDaySmoker, "Depression epissode in days for everyday smoker" ,'S4AQ9DR')
    smoke_5_to_6 = data[data['S3AQ3B1'] == 2] 
    printFormattedData(smoke_5_to_6, "Depression epissode in days for smoker of 5 to 6 cogarretes" ,'S4AQ9DR')
    smoke_3_to_4 = data[data['S3AQ3B1'] == 3] 
    printFormattedData(smoke_3_to_4, "Depression epissode in days for smoker of 3 to 4 cogarretes",'S4AQ9DR')
    smoke_1_to_2 = data[data['S3AQ3B1'] == 4] 
    printFormattedData(smoke_1_to_2, "Depression epissode in days for smoker of 1 to 2 cogarretes",'S4AQ9DR')
    smoke_2_to_3 = data[data['S3AQ3B1'] == 5] 
    printFormattedData(smoke_2_to_3, "Depression epissode in days for smoker of 2 to 3 cogarretes",'S4AQ9DR')
    smoke_once_a_month = data[data['S3AQ3B1'] == 6]
    printFormattedData(smoke_once_a_month, "Depression epissode in days for never or unknown smoker",'S4AQ9DR')

def printInitialCorreletion(data):
    print ("Printing Initial correlcation")
    printDepressedAndSmoking(data)

def updateData(data):
    updatingSmokingData(data)
    updateIndividualDepression(data)
    updateFamilyDepression(data)
    
def printData(data):
    printSmokingdistribution(data)
    printIndividualDepression(data)
    printFamilyDepression(data)  

def printReport(dataFile):
    os.path.dirname(os.path.abspath(__file__))
    data = pandas.read_csv(dataFile, low_memory=False)
    updateData(data)
    printData(data)
    printInitialCorreletion(data)

def main():
    printReport(dataFile)


if __name__ == "__main__":
    main()
    os.system("pause")