#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
#        python3 mcb.pyw <keyword> - Loads keyword to clipboard.
#        python3 mcb.pyw list - Loads all keywords to clipboard.
#        python3 mcb.pyw delete - Delete all keyword
#        python3 mcb.pyw delete <keyword> - Delete keyword

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
  keyword = sys.argv[2]
  if sys.argv[1].lower() == 'save':
    mcbShelf[keyword] = pyperclip.paste()
  else:
    del mcbShelf[keyword]
elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
  elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])
  elif sys.argv[1].lower() == 'delete':
    mcbShelf.clear()

mcbShelf.close()
