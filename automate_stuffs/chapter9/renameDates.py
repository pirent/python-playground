#!/usr/bin/python3
# renameDates.py - rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY
import shutil, os, re

# create a regex that maches files with the American date format.
datePattern = re.compile(r"""^(.*?) 	# all text before date
  ((0|1)?\d)-				# one or two digits for the month
  ((0|1|2|3)?\d)-			# one or two digits for the day
  ((19|20)\d\d)				# four digits for the year
  (.*?)$
  """, re.VERBOSE)

# loop over the files in the working directory
for amerFilename in os.listdir('.'):
  mo = datePattern.search(amerFilename)

  # skip files without date
  if mo == None:
    continue

  # get the different parts of the filename
  beforePart = mo.group(1)
  monthPart = mo.group(2)
  dayPart = mo.group(4)
  yearPart = mo.group(6)
  afterPart = mo.group(8)

  # form the European-style filename
  euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

  # get the full, absolute file path
  absWorkingDir = os.path.abspath('.')
  amerFilename = os.path.join(absWorkingDir, amerFilename)
  euroFilename = os.path.join(absWorkingDir, euroFilename)

  # rename the files
  print('Renaming "{}" to "{}" ...'.format(amerFilename, euroFilename))
  shutil.move(amerFilename, euroFilename)
