import os
from datetime import datetime
from collections import deque
# Set duration to start
start_duration=datetime.now()
# set global values
iscsv=0
isdev=0
# Get the contextual path from drive
# filepath='..\PythonPractice'
filepath='E:\TestData'
outpath = 'e:\TestDataOutPut\\'
print os.getcwd()
lists= deque(os.listdir(filepath))
print lists
print os.listdir(os.getcwd())
# set path for input and output
def setPath():
    global outpath
    global filepath
    if isdev==1 :
        outpath = 'e:\TestDataOutPut\\'
        filepath='E:\TestData'
    else:
        outpath = 'e:\SC_Flood_Data\Json_OutPut\\'
       filepath='E:\SC_Flood_Data\json'
# Get files in specified path
def GetFolderData():
    global lists
    lists= os.listdir(filepath)
class TextFile(object):
    def __init__(self,filename, mode):
        self.count = 0
        self.txtfileObj = codecs.open(outpath + filename + ".txt", mode,'utf-8')
    @property
    def increment(self):
       self.count +=1
       return self.count
    
# set filters
state="South Carolina"
fromdate="2015-10-02"
todate="2015-10-16"
unitedStates="United States"
nonUnitedStates="Non_UnitedStates"
notAvailable="NA"
nonState="Non_SouthCarolina"
txtfileObj=None
date_txt_objects={}
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
    statetxtfile=TextFile(state.replace(" ","_"),'a')
    nonStatetxtfile=TextFile(nonState,'a')
    unitedStatestxtfile=TextFile(unitedStates,'a')
    nonUnitedStatesTextFile=TextFile(nonUnitedStates,'a')
    notAvailableCountryTextFile=TextFile(notAvailable,'a')
# Region and date specific
def GetStateDateTextFile(curstate,curdate):
    date_filename=curstate+'_'+curdate
    if date_filename not in date_txt_objects.keys():
       date_txt_objects[date_filename]=TextFile(date_filename,'a')
    return date_txt_objects[date_filename]
    
    
# Get JSON to extracted data
# print Extracted Data from Json files
# All required data
def printExtractedDataToText(txtObj) :
    count= txtObj.increment
    body_text = body.replace('\n',' ')
    txtObj.txtfileObj.write(str(count)+','+str(count)+body_text+'\n')
'''
=========================================================
BEGIN THE FLOOD DATA EXTRACTION
=========================================================
'''
# Set Input and Output FilePaths
setPath()
# get input data files
GetFolderData()
createtxtFiles()
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
                if country:
                    if country==unitedStates:
                        # United States country
                        printExtractedDataToText(unitedStatestxtfile)
                        if region==state:
                            # South Carolina State
                            printExtractedDataToText(statetxtfile)
                            if objectpostedtime[:10] > fromdate and  objectpostedtime[:10]< todate:
                                printExtractedDataToText(GetStateDateTextFile(state,objectpostedtime[:10]))
                        else :
                            # Non-SouthCarolina States
                            printExtractedDataToText(nonStatetxtfile)
                            if objectpostedtime[:10] > fromdate and  objectpostedtime[:10]< todate:
                                printExtractedDataToText(GetStateDateTextFile(nonState,objectpostedtime[:10]))
                    else :
                        # Non United States Countries
                        printExtractedDataToText(nonUnitedStatesTextFile)
                else :
                    # Country Not Available
                    printExtractedDataToText(notAvailableCountryTextFile)
print datetime.now()-start_duration
print size/((1024**2)*1.0)
