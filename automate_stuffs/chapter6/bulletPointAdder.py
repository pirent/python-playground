#!/usr/bin/python3
# bulletPointAdder.py - Adds Markdown bullet points to the start
# of each line of text of the clipboard

import pyperclip

text = pyperclip.paste()

# Separate line and stars.
text = "line1\nline2\nline3"
lines = text.split('\n')
for i in range(len(lines)):
  lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
