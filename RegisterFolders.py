"""Save all subdirectories in your target directory to a .csv and .json file. This file can later
be used to recreate your directory."""

import os
import json

def RegisterFolders(directoryToProcess, NewRegisteredName="Untitled"):
    subdirs = [x[0] for x in os.walk(directoryToProcess)]
    rel = [os.path.relpath(subdir,directoryToProcess).replace("\\","/") for subdir in subdirs]
    rel.remove('.')
    outdict = {"Name":NewRegisteredName,"Folders": rel}
    return outdict
    
def SaveRegisteredFolders(filepath,dict_):
    filepathbase = os.path.splitext(filepath)[0]
    # # Save Json Version
    with open(filepathbase+'.json', 'w') as outfile:
        json.dump(dict_, outfile, indent=4)
    
    # # Save CSV Version
    csvString = '\n'.join(dict_['Folders'])
    with open(filepathbase+'.csv', 'w') as outfile:
        for folder in csvString:
            outfile.write(folder)
        

if __name__ == '__main__':
    registerdFolders = RegisterFolders('M:/Projects/temp/newProject')
    SaveRegisteredFolders(os.path.dirname(__file__)+"\configs\shot.json", registerdFolders)