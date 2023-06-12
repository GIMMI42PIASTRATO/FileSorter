# FileSorter
This is a Python script that monitors a specified folder and automatically moves files to different folders based on their file extensions. The script uses the Watchdog library to monitor file system events and performs the sorting operation when a new file is created in the observed folder.

## Setup
Before running the script, make sure to modify the FOLDER_TO_WATCH variable to specify the path of the folder you want to monitor. You can change this path by updating the value assigned to the variable:<br>
```
FOLDER_TO_WATCH = "D:\Tutti i file\Programmazione di Vittorio\Python\FileSorter\Hopper"
```

## Sorting Logic
The script uses a mapping of file extensions to destination folders to determine where each file should be moved. By default, the script supports .txt, .png, and .jpg file types. You can add more file extensions and associate them with specific destination paths by modifying the dir_path dictionary in the findThePath function:<br>
```
dir_path = {
    ".txt": "D:\\Tutti i file\\Programmazione di Vittorio\\Python\\FileSorter\\FileTXT",
    ".png": "D:\\Tutti i file\\Programmazione di Vittorio\\Python\\FileSorter\\Immagini",
    ".jpg": "D:\\Tutti i file\\Programmazione di Vittorio\\Python\\FileSorter\\Immagini",
}[f".{file_extension}"]
```
You can add more extensions as keys and associate a path as the corresponding value to support additional file types and move them to specific folders.

## Event Handling
The EventHandler class extends FileSystemEventHandler from the Watchdog library. It overrides the on_created method to handle the file creation event. When a new file is created in the observed folder, the script prints the path of the created file and attempts to move it to the appropriate destination folder based on its extension.

If the file is successfully moved, the script prints the new location of the file. If the destination folder is empty or not found in the dir_path dictionary, an appropriate message is printed.

## Running the Script
After setting up the script with the correct folder path and desired sorting logic, you can run it. The script starts an observer to monitor the specified folder for file creation events. It runs continuously until interrupted by the user.

To run the script, execute the Python file containing the code. The script will continuously monitor the folder and automatically sort the files based on their extensions.<br>
```
python file_sorter.py
```
To stop the script, press Ctrl+C in the terminal.

Note: Make sure you have the necessary permissions to read from and write to the observed folder and destination folders.
