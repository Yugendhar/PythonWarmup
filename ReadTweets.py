import json
import codecs
import os
from datetime import datetime
from collections import deque

# Set duration to start
start_duration=datetime.now()

# set global values
iscsv=0
isdev=1

# Get the contextual path from drive
# filepath='..\PythonPractice'
filepath='G:\TestData'
outpath = 'g:\TestDataOutPut\\'

print os.getcwd()
lists= deque(os.listdir(filepath))
print lists
print os.listdir(os.getcwd())

# set path for input and output
def setPath():
    global outpath
    global filepath
    if isdev==1 :
        outpath = 'g:\TestDataOutPut\\'
        filepath='G:\TestData'
    else:
        outpath = 'g:\SC_Flood_Data\Json_OutPut\\'
        filepath='G:\SC_Flood_Data\json'

txtfileObj=None

# Get files in specified path
def GetFolderData():
    global lists
    lists= os.listdir(filepath)




# set filters
state="South Carolina"
fromdate="2015-10-02"
todate="2015-10-16"
unitedStates="United States"
nonUnitedStates="Non_UnitedStates"
notAvailable="NA"
nonState="Non_SouthCarolina"


'''
================================
Create and Write Text Files
================================
'''

'''
===========================================
Create and Write to Text Files
===========================================
'''

# Text data files
worldtxtfile=None
statetxtfile=None
datetxtfile=None
unitedStatestxtfile=None
nonStatetxtfile=None
nonUnitedStatesTextFile=None
notAvailableCountryTextFile=None

# create txt files
def createtxtFiles():
    global statetxtfile
    global nonStatetxtfile
    global unitedStatestxtfile
    global nonUnitedStatesTextFile
    global notAvailableCountry
    global notAvailableCountryTextFile

    #worldtxtfile=createTextFile("world")
    statetxtfile=createTextFile(state.replace(" ","_"),'a')
    nonStatetxtfile=createTextFile(nonState,'a')
    unitedStatestxtfile=createTextFile(unitedStates,'a')
    nonUnitedStatesTextFile=createTextFile(nonUnitedStates,'a')
    notAvailableCountryTextFile=createTextFile(notAvailable,'a')


# Creating a Txt file
def createTextFile(filename,mode):
    txtfileObj = codecs.open(outpath + filename + ".txt", mode,'utf-8')
    return txtfileObj

# Region and date specific
def GetStateDateTextFile(curstate,curdate):
    return createTextFile(curstate+'_'+curdate,'a')

# Get JSON to extracted data
# print Extracted Data from Json files
# All required data
def printExtractedDataToText(txtObj) :
    body_text = body.replace('\n',' ')
    txtObj.write(body_text+'\n')


'''
=========================================================
BEGIN THE FLOOD DATA EXTRACTION
=========================================================
'''
# Set Input and Output FilePaths
setPath()

# get input data files
GetFolderData()
size=0
for f in lists :
    with open(filepath+'\\'+f) as json_data :
        size=size+os.path.getsize(filepath+'\\'+f);
        for line in json_data :
            # Intialization of collected variables
            actorlocation = ""
            actorpostedtime = ""
            actorsummary = ""
            body = ""
            objectpostedtime = ""
            objectsummary = ""
            language = ""
            country = ""
            region = ""
            locality = ""

            try :
                #loads JSON data
                data=json.loads(line)
            except ValueError,e:
                continue
            if "body" in data:
                body=data["body"]

            if "object" in data:
                objectpostedtime=data["object"]["postedTime"]
                if "summary" in data["object"]:
                    objectsummary=data["object"]["summary"]
            if "gnip" in data:
                if "language" in data["gnip"] :
                    language=data["gnip"]["language"]["value"]
                if "profileLocations" in data["gnip"]:
                    country=data["gnip"]["profileLocations"][0]["address"]["country"]
                    if "region" in data["gnip"]["profileLocations"][0]["address"]:
                        region=data["gnip"]["profileLocations"][0]["address"]["region"]
                    if "locality" in data["gnip"]["profileLocations"][0]["address"] :
                        locality=data["gnip"]["profileLocations"][0]["address"]["locality"]
                createtxtFiles()
                if country:
                    if country==unitedStates:
                        # United States country
                        printExtractedDataToText(unitedStatestxtfile)
                        if region==state:
                            # South Carolina State
                            printExtractedDataToText(statetxtfile)
                            if objectpostedtime[:10] > fromdate and  objectpostedtime[:10]< todate:
                                printExtractedDataToText(GetStateDateTextFile(state,objectpostedtime[:10]))
                        else :
                            # Non-SouthCarolina States
                            printExtractedDataToText(nonStatetxtfile)
                            if objectpostedtime[:10] > fromdate and  objectpostedtime[:10]< todate:
                                printExtractedDataToText(GetStateDateTextFile(nonState,objectpostedtime[:10]))
                    else :
                        # Non United States Countries
                        printExtractedDataToText(nonUnitedStatesTextFile)
                else :
                    # Country Not Available
                    printExtractedDataToText(notAvailableCountryTextFile)

print datetime.now()-start_duration
print size/((1024**2)*1.0)
