from watchdog.observers import Observer
from watchdog.events import *
import time
import re
import v
import os,sys, stat
class FileEventHandler(FileSystemEventHandler):
  def __init__(self):
    FileSystemEventHandler.__init__(self)

  # def on_any_event(self, event):
  #   print(event)
  #
  # def on_moved(self, event):
  #   if event.is_directory:
  #     print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
  #   else:
  #     print("file moved from {0} to {1}".format(event.src_path, event.dest_path))
  # def on_created(self, event):
  #   if event.is_directory:
  #     print("directory created:{0}".format(event.src_path))
  #   else:
  #     print("file created:{0}".format(event.src_path))
  # def on_deleted(self, event):
  #   if event.is_directory:
  #     print("directory deleted:{0}".format(event.src_path))
  #   else:
  #     print("file deleted:{0}".format(event.src_path))

  def on_modified(self, event):
    if event.is_directory:
      print("directory modified:{0}".format(event.src_path))
    else:
      print("file modified:{0}".format(event.src_path))
      # print(os.path.exists(event.src_path))
      path = event.src_path.partition('html')[0] + event.src_path.partition('html')[1]
      print(path)
      os.chmod(url,stat.S_IRWXO)
      if event.src_path.find('html') > 0:
       v.v(path)


if __name__ == "__main__":
  observer = Observer()
  event_handler = FileEventHandler()
  observer.schedule(event_handler, "ac/pc", recursive=True)
  observer.start()
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

