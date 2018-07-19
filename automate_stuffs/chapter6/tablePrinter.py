#!/usr/bin/python3
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
  # find the longest string in each inner list
  # so that the whole column can be wide enough to fit all
  colWidths = []
  for i in range(len(data)):
    colWidths.append(getTheLongestStringLen(data[i]))
  
  # get size of inner list that has most elements
  max_size = 0
  for il in tableData:
    if max_size < len(il):
      max_size = len(il)

  # use that max_size var as number of rows
  rows = max_size
  
  for row in range(rows):
    line = []
    for col in range(len(tableData)):
      cell = tableData[col][row]
      line.append(cell.rjust(colWidths[col]))
    printLine(line)

def getTheLongestStringLen(il):
  longest = 0
  for s in il:
    if len(s) < longest:
      longest = len(s)
  return longest

def printLine(line):
  print(' '.join(line))

# ========================
    
printTable(tableData)    
