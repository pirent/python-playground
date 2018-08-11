#!/usr/bin/python3
# Write a program that walks through a folder tree and searches for exceptionally large files or folders
# say, ones that have a file size of more than the provided input 
# Print these files with their absolute path to the screen
import os, shutil

def look_for_large_file(folder, size_of_large_file):
  
  """
  parameter:
    folder: the directory to walk through
    size_of_large_file: in megabyte
  """
  for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
      folder = os.path.abspath(folder)  # make sure folder is absolute
      filename = os.path.join(folder, filename)
      filesize = round(os.path.getsize(filename) / 1000000, 2)
      if filesize > size_of_large_file:
        print("File size of {} is {} MB".format(filename, filesize))
    
if __name__ == "__main__":
  look_for_large_file(".")
