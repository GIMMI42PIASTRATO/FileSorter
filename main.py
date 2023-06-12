import watchdog.events as eventsModule
import watchdog.observers.polling as observerModule
import time
import os

FOLDER_TO_WATCH = "D:\Tutti i file\Programmazione di Vittorio\Python\FileSorter\Hopper"  # CHANGE THE PATH TO CHANGE THE OBSERVED FOLDER


class EventHandler(eventsModule.FileSystemEventHandler):
    def dispatch(self, event: eventsModule.FileSystemEvent):
        if event.event_type == None:
            print(f"Event type: None")
            return

        super().dispatch(event)

    def on_created(self, event: eventsModule.FileSystemEvent):
        print(f"File created: {event.src_path}")
        path = findThePath(event.src_path)
        if path:
            os.rename(event.src_path, path)
            print(f"File moved to location: {path}")
        else:
            print(f"{path} is a empty directory")


def findThePath(scr_path: str):
    if os.path.isfile(scr_path):
        file_name, file_extension = os.path.basename(scr_path).split(".")
        dir_path = {
            # add more extensions as keys and associate a path as a value to add more supported files and be able to move them into certain folders
            ".txt": "D:\\Tutti i file\\Programmazione di Vittorio\\Python\\FileSorter\\FileTXT",
            ".png": "D:\\Tutti i file\\Programmazione di Vittorio\\Python\\FileSorter\\Immagini",
            ".jpg": "D:\\Tutti i file\\Programmazione di Vittorio\\Python\\FileSorter\\Immagini",
        }[f".{file_extension}"]

        return f"{dir_path}\{file_name}.{file_extension}"  # return the new path

    # for element in os.listdir(scr_path):
    #     new_element = f"{scr_path}\{element}"

    #     if os.path.isfile(new_element):
    #         return findThePath(new_element)
    #     else:
    #         return findThePath(new_element)


eventHandler = EventHandler()
observer = observerModule.PollingObserver(1)
observer.schedule(eventHandler, FOLDER_TO_WATCH, recursive=True)
observer.start()

try:
    while True:
        time.sleep(3)
except KeyboardInterrupt:
    observer.stop()

observer.join()
