import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_created = self.on_created
        self.observer = Observer()

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".csv"):
            print(f"New CSV file detected: {event.src_path}")
            self.run_predict_script(event.src_path)

    def run_predict_script(self, file_path):
        time.sleep(2)
        try:
            script_path = "/Users/hamzabenaggoun/Desktop/HomeShieldAI/anomaly_detection/predict.py"
            print(f"Running prediction on {file_path}")
            subprocess.run(["python", script_path, file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running prediction script: {e}")

    def start(self):
        self.observer.schedule(self.event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        print(f"Monitoring {self.DIRECTORY_TO_WATCH} for new CSV files...")
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping directory monitor...")
            self.observer.stop()
        self.observer.join()

if __name__ == "__main__":
    directory_to_watch = "/Users/hamzabenaggoun/Desktop/HomeShieldAI/flow_output" 
    watcher = Watcher(directory_to_watch)
    watcher.start()
