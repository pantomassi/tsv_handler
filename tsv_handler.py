import os
import signal
import time
from datetime import datetime
from tkinter import messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler


user_tag = os.getcwd().split("\\")[2]
download_dir = r"C:\\Users\\" + user_tag + r"\\Desktop\\Download"
tsv_dir = download_dir + r"\\tsv"
error_msg = "tsv_handler has stopped working. Check error_log.txt in 'tsv' folder and restart the app"
error_log_file = tsv_dir + r"\\" + "error_log.txt"


def log_error_and_close(error_desc):
	with open(error_log_file, "a") as log:
		log.write(f"{datetime.now()}: {str(error_desc)}\n\n")
	messagebox.showerror("Error", error_msg)
	os.kill(os.getpid(),signal.SIGTERM)


class DownloadHandler(FileSystemEventHandler):
	def on_created(self, event):
		try:
			time.sleep(1.75) #without sleep(), the newly created file will not be found yet
			for filename in os.listdir(download_dir):
				if filename.startswith("fnd_gfm_") and filename.endswith(".tsv"):
					downloaded_tsv_path = download_dir + r"\\" + filename
					new_tsv_path = tsv_dir + r"\\" + datetime.now().strftime("tsv_%d-%m-%Y-%H-%M-%S") + ".tsv"
					os.rename(downloaded_tsv_path, new_tsv_path)
		except Exception as Argument:
			log_error_and_close(Argument)


class TsvHandler(PatternMatchingEventHandler):
	patterns = ["tsv_*.tsv"]

	def on_created(self, event):
		try:
			time.sleep(1.75) #without sleep(), the newly created file will not be found yet
			downloaded_tsvs = [file for file in os.listdir(tsv_dir)]
			downloaded_tsvs.sort(reverse=True)
			tsv_to_open_path = tsv_dir + r"\\" + downloaded_tsvs[0]
			os.startfile(tsv_to_open_path)
		except Exception as Argument:
			log_error_and_close(Argument)


event_handler1 = DownloadHandler()
observer1 = Observer()
observer1.schedule(event_handler1, download_dir, recursive=True)
observer1.start()

event_handler2 = TsvHandler()
observer2 = Observer()
observer2.schedule(event_handler2, tsv_dir, recursive=True)
observer2.start()

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer1.stop()
	observer2.stop()
observer1.join()
observer2.join()




