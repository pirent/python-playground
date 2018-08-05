#!/usr/bin/python3
# madlibs.py - read in text files and let user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB or VERB appears in the text file.
# The results should be printed to the screen and saved to a new text file.
#
# Usage: madlibs <filepath>
import os, sys, re

if len(sys.argv) < 2:
  print("Usage: madlibs <filepath>")
  exit(1)

filepath = sys.argv[1]
if not os.path.exists(filepath):
  print("File is not existed")
  exit(1)

HOLDER = {'ADJECTIVE', 'NOUN', 'ADVERB', 'VERB'}
PATTERN = re.compile(r'ADJECTIVE?|NOUN?|ADVERB?|VERB?')
VOWELS = 'AEIOU'

fileObj = open(filepath)
origin = fileObj.read().split()
fileObj.close()

for index, word in enumerate(origin):
  mo = re.match(PATTERN, word)
  if mo:
    article = 'an' if word[0] in VOWELS else 'a'
    word_to_replace = input('Enter {} {}:\n'.format(article, mo.group().lower()))
    origin[index] = PATTERN.sub(word_to_replace, word)
  
newContent = ' '.join(origin)
print("After replacing: " + newContent)
fileObj = open('./modified', 'w')
fileObj.write(newContent)
fileObj.close()
