# Description
2 Tools for pipeline use.

# FoldersFromMarkers

## Description
Convert a .csv Marker file exported from Adobe Premiere into appropriate pipeline folders.

## Usage
```python
import os
from FoldersFromMarkers import ReadCSV, CreateFolders

data = ReadCSV(filepath='Harvey-30_01.csv',targetcolumn=0,startingrow=1)
CreateFolders(outputFolder=os.path.dirname(__file__), data=data,shotsSpawnedFoldersConfigPath='configs/shot.csv')

```
## ReadCSV
- filepath
  - The filepath of the .csv to process
- targetcolumn
  - The index of the name column
- startingrow
  - The row the data starts, not the header.

## CreateFolders
- outputFolder
  - The directory you want to create the new folders in based on the .csv.
- data
  - The data returned from ReadCSV in the form of ```tuple(str,dict) example: ('Intro001000', {})```
- shotsSpawnedFoldersConfigPath
  - .csv file that has folders to create for the shot directories.

# RegisterFolders

## Description
Save all subdirectories in your target directory to a .csv and .json file. This file can later
be used to recreate your directory.

## Usage
```python
import os
from RegisterFolders import RegisterFolders, SaveRegisteredFolders

registerdFolders = RegisterFolders('M:/Projects/temp/newProject')
SaveRegisteredFolders(os.path.dirname(__file__)+"\configs\shot.json", registerdFolders)

```
## Output
```json
{"Name":"Untitled","Folders":["assets","assets/geo"]}
```
## RegisterFolders
- directoryToProcess
  - The directory you want to process
- NewRegisteredName
  - The name to register all the folders as.
  
## SaveRegisteredFolders
- outputFolder
  - The directory you want to save the .csv and .json to.
- dict_
  - The data returned from ReadCSV in the form of ```dict example: {"Name":"Untitled","Folders":["assets","assets/geo"]}```