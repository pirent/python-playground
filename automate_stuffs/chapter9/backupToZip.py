#!/usr/bin/python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
import zipfile, os

def backupToZip(folder):
  # backup the entire contents of "folder" into a ZIP file.

  folder = os.path.abspath(folder)

  # figure out the filename this code should use
  # based on what files already exist.
  number = 1
  while True:
    zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipFilename):
      break
    number += 1
  
  # create the zip file
  print('Creating {}...'.format(zipFilename))
  backupZip = zipfile.ZipFile(zipFilename, 'w')
  
  # walk the entire folder tree and compress the files in each folder
  for foldername, subfolders, filenames in os.walk(folder):
    print('Adding files in {}...'.format(foldername))
   
     # add the current folder to the ZIP file
    backupZip.write(foldername)

    # add all the files in this folder to the ZIP file
    for filename in filenames:
      newBase = os.path.basename(folder) + '_'
      if filename.startswith(newBase) and filename.endswith('.zip'):
        # don't backup the backup ZIP files
        continue 	
      backupZip.write(os.path.join(foldername, filename))

    backupZip.close()

  print('Done')

if __name__ == '__main__':
  backupToZip('/tmp/delicious')
