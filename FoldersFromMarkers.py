"""Convert a .csv Marker file exported from Adobe Premiere into appropriate pipeline folders."""

import os
import json
import re

def ReadCSV(filepath, targetcolumn=0, startingrow=1):

    file = open(filepath, 'r',encoding='utf-16')
    csvdataLines = file.readlines()
    file.close()
    headers = [header for header in csvdataLines[0].replace("\n",'').split('\t')]
    outdata = []
    outdata = []
    for row in range(startingrow,len(csvdataLines)):
        roww = csvdataLines[row]
        spl = roww.split('\t')
        js = ToJSONData(headers,spl)
        outdata.append((spl[targetcolumn].replace("\n",''), js))
    return outdata

def ToJSONData(headers, values):
    outjs = {}
    for indx, header in enumerate(headers):
        if header != '':
            outjs[header] = values[indx]
    return outjs

def SplitName(name):
    match = re.match(r"([a-z]+)([0-9]+)", name, re.I)
    if match:
        items = match.groups()
        return items
    return None

def CreateFolders(outputFolder, data, shotsSpawnedFoldersConfigPath='configs/shot.csv'):
    namedirs = []
    for  name, dictData in data:
        split = SplitName(name)
        dictData['Sequence'] = split[0]
        dictData['ShotID'] = split[1]
        dictData['ShotName'] = name
        if split[0]:
            if split[0] in namedirs == False:
                namedirs.append(SplitName(name))
    folders = GetFoldersFromCSV(shotsSpawnedFoldersConfigPath)
    for  name, dictData in data:
        nameSplit = SplitName(name)
        newOutFolder = os.path.join(outputFolder, nameSplit[0])
        newDir = os.path.join(newOutFolder, name)
        seqconfig = os.path.join(newDir, 'shot_config.json')
        if os.path.exists(newDir) == False:
            os.makedirs(newDir)
        
        CreateFoldersFromList(folders,newDir )

        with open(seqconfig, 'w') as outfile:
            json.dump(dictData, outfile, indent=4)
        # file = open(seqconfig, 'w')
        # file.write(js)
        # file.close()
        
def GetFoldersFromCSV(shotsSpawnedFoldersConfigPath='configs/shot.csv'):
    file = open(shotsSpawnedFoldersConfigPath, 'r')
    csvdataLines = file.readlines()
    file.close()
    outlines = [column.split('\t')[0].replace("\n", "") for column in csvdataLines]
    v=0
    return outlines
    
def CreateFoldersFromList(Folders, outputFolder):
    for folder in Folders:
        newdir = os.path.join(outputFolder, folder)
        if os.path.exists(newdir) == False:
            os.makedirs(newdir)
            
        


def main():
    data = ReadCSV(filepath='Harvey-30_01.csv',targetcolumn=0,startingrow=1)
    CreateFolders(outputFolder='M:/Projects/Chemours/VLTDMSCCH2202H/Sequence', data=data,shotsSpawnedFoldersConfigPath='configs/shot.csv')
    
    # CreateFolders(outputFolder=os.path.dirname(__file__), data=data)


if __name__ == '__main__':
    main()

    