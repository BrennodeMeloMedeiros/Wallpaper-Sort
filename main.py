# https://stackoverflow.com/questions/21715895/creating-a-background-changer-in-python-with-ctypes-not-working
# https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10
# https://stackoverflow.com/questions/30071886/how-to-get-current-time-in-python-and-break-up-into-year-month-day-hour-minu


import ctypes
import os 
import random
import json
from dateTime import *


SPI_SETDESKWALLPAPER = 20


date = str(getDay())
imgPath = r"C:\Users\brenn\Wallpaper Sort\WPP"

with open(r"C:\Users\brenn\Wallpaper Sort\data.json", 'r') as data:

    foldersResgister = json.load(data)

    # See if there isnt already a chosen folder for the current day
    if "date" in foldersResgister and foldersResgister["date"] == date:
        chosenFolderFullPath = foldersResgister["folder"]
    else:      
        # Sort the folder for the day
            # "next(os.walk(imgPath))[1]" get all the fodler from the directory.
            # "next(os.walk(imgPath))[2]"" get all the files from the directory.
        totalWppFolders = len(next(os.walk(imgPath))[1])
        drawnedFolderNumber = random.randint(1,totalWppFolders)
        chosenFolder = next(os.walk(imgPath))[drawnedFolderNumber][0]

        chosenFolderFullPath = f"{imgPath}\{chosenFolder}"
        
# Register the chosen folder
with open(r"C:\Users\brenn\Wallpaper Sort\data.json", 'w') as data:
    objChosenFolder = {
        "date": date,
        "folder": chosenFolderFullPath
    }
    json.dump(objChosenFolder,data)

    
# Once the folder has been chosen, its time to select the image

totalWppImages = len(next(os.walk(chosenFolderFullPath))[2])

if totalWppImages > 0:
    chosenFolderName = chosenFolderFullPath.split("\\")[-1]

    if chosenFolderName == "byDayTime":
        timeZone = getTimeZone()
        print(timeZone)
        chosenImageFullPath = f'{chosenFolderFullPath}\{timeZone}.jpg'
    else:
        drawnedImageNumber = random.randint(0,totalWppImages - 1)
        chosenImageName = next(os.walk(chosenFolderFullPath))[2][drawnedImageNumber]
        chosenImageFullPath = f'{chosenFolderFullPath}\{chosenImageName}'
else:
    chosenImageFullPath = f'{imgPath}\error.jpg' 
    print("No images were found in the chosen folder =/")
print(f"{imgPath}\{chosenImageFullPath}")
ctypes.windll.user32.SystemParametersInfoW(20, 0, chosenImageFullPath , 0)
