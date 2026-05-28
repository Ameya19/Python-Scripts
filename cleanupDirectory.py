import os
from pathlib import Path
import shutil

pathToDirectory = "" #Give the path to the directory you want to clean up here

extensionsToFolders = {
    ".pdf": "PDFs",
    ".docx": "Word Documents",
    ".xlsx": "Excel Spreadsheets",
    ".xls": "Excel Spreadsheets",
    ".epub": "eBooks",
    ".zip": "Archives",
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".exe": "Executables",
    ".torrent": "Torrents",
    ".txt": "Text Files",
    ".csv": "Text Files",
}

for filename in os.listdir(pathToDirectory):
    filePath = os.path.join(pathToDirectory, filename)
    extension = Path(filePath).suffix.lower()
    if extension in extensionsToFolders:
        folderPath = os.path.join(pathToDirectory, extensionsToFolders[extension])
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        shutil.move(filePath, folderPath)
