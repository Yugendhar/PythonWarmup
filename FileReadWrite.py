import math
#a= raw_input()


import json
import unicodecsv as csv
import codecs
import os


#Get the contextual path from drive
#E:\Py-Workspace\PythonPractice
#filepath='..\PythonPractice'

#E:\TestData

filepath='G:\SC_Flood_Data\json'
print os.getcwd()
lists= os.listdir(filepath)
print lists
print os.listdir(os.getcwd())

print '^^^^^^^'


#'e:\TestDataOutPut\\'
outpath = 'g:\SC_Flood_Data\Json_OutPut\\'
csvObj=None
txtfileObj=None
iscsv=0
isdev=1





#set path for input and output
def setPath():
    global outpath
    global filepath
    if isdev==1 :
        outpath = 'e:\TestDataOutPut\\'
        filepath='E:\TestData'
    else:
        outpath = 'g:\SC_Flood_Data\Json_OutPut\\'
        filepath='G:\SC_Flood_Data\json'

#Get files in specified path
def GetFolderData():
    global lists
    lists= os.listdir(filepath)

#Creating a CSV file
def createFile(filename):
    csvopenfile = open(outpath + filename + ".csv", 'wb')
    csvObj = csv.writer(csvopenfile, encoding='utf-8');
    csvObj.writerow(["ActorLocation", "ActorPosteTime", "ActorSummary",
                     "Body", "ObjectPostedTime", "ObjectSummary", "Language",
                     "Country", "Region", "Locality"])
    return csvObj




# Get JSON to extracted data
# print Extracted Data from Json files
# All required data

def printExtractedData(csvObj) :
    csvObj.writerow([actorlocation, actorpostedtime, actorsummary,
                     body, objectpostedtime, objectsummary, language,
                     country, region, locality])

# Get JSON to extracted data
# print Extracted Data from Json files
# All required data

def printExtractedDataToText(txtObj) :
    txtObj.write(body+'\n')

state="South Carolina"
fromdate="2015-10-02"
todate="2015-10-16"

#csv data
worldcsvfile=None
statecsvfile=None
datecsvfile=None

#create csv files
def createcsvFiles():
    global statecsvfile
    global datecsvfile
    #worldcsvfile=createFile("world")
    statecsvfile=createFile(state.replace(" ","_"))
    datecsvfile=createFile(fromdate+'_'+todate)

#txt data
worldtxtfile=None
statetxtfile=None
datetxtfile=None

#create txt files
def createtxtFiles():
    global statetxtfile
    global datetxtfile
    #worldtxtfile=createTextFile("world")
    statetxtfile=createTextFile(state.replace(" ","_"),'a')

# Creating a Txt file
def createTextFile(filename,mode):
    txtfileObj = codecs.open(outpath + filename + ".txt", mode,'utf-8')
    return txtfileObj

def GetStateDateTextFile(curdate):
    return createTextFile(state+'_'+curdate,'a')

'''
=========================================================
BEGIN THE DATA EXTRACTION
=========================================================
'''

#to Do : delete all output files before a fresh start
setPath()

#get input data files
GetFolderData()

for f in lists :
    with open(filepath+'\\'+f) as json_data :
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
                #loads data
                data=json.loads(line)
            except ValueError,e:
                #print'<<<<<<>>>>>>>>>'
                #print line
                #print('<<<<<<<'+str(e)+ '>>>>>>>')
                continue
                #data=json.load(json_data)
                # print '---------------'
                # print '---------------'
                # print(data)

            if "actor" in data:
                if "location" in data["actor"]:
                    actorlocation=data["actor"]["location"]["displayName"]
                    #print(data["actor"]["location"]["displayName"])
                actorpostedtime=data["actor"]["postedTime"]
                actorsummary=data["actor"]["summary"]
                #print(data["actor"]["postedTime"])
                #print(data["actor"]["summary"])

                # print '---body and Object summary---'
            if "body" in data:
                body=data["body"]
                #print(data["body"])
            if "object" in data:
                objectpostedtime=data["object"]["postedTime"]
                # print(data["object"]["postedTime"])
                # print(objectpostedtime[:10])
                if "summary" in data["object"]:
                    objectsummary=data["object"]["summary"]
                    #print(data["object"]["summary"])
            if "gnip" in data:
                if "language" in data["gnip"] :
                    language=data["gnip"]["language"]["value"]
                    #print(data["gnip"]["language"]["value"])
                if "profileLocations" in data["gnip"]:
                    country=data["gnip"]["profileLocations"][0]["address"]["country"]
                    #print(data["gnip"]["profileLocations"][0]["address"]["country"])
                    if "region" in data["gnip"]["profileLocations"][0]["address"]:
                        region=data["gnip"]["profileLocations"][0]["address"]["region"]
                        #print(data["gnip"]["profileLocations"][0]["address"]["region"])
                    if "locality" in data["gnip"]["profileLocations"][0]["address"] :
                        locality=data["gnip"]["profileLocations"][0]["address"]["locality"]
                        #print(data["gnip"]["profileLocations"][0]["address"]["locality"])

            #print '--------------'
            if iscsv:
                createcsvFiles()
                printExtractedData(worldcsvfile)
                if region==state:
                    printExtractedData(statecsvfile)
                    if objectpostedtime[:10] > fromdate and  objectpostedtime[:10]< todate:
                        printExtractedData(datecsvfile)
            else :
                createtxtFiles()
                if region==state:
                    printExtractedDataToText(statetxtfile)
                    if objectpostedtime[:10] > fromdate and  objectpostedtime[:10]< todate:
                        printExtractedDataToText(GetStateDateTextFile(objectpostedtime[:10]))


