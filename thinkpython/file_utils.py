import os

def walk(dirname):
  for name in os.listdir(dirname):
    path = os.path.join(dirname, name)
    
    if os.path.isfile(path):
      print(path)
    else:
      walk(path)

def walk2(dirname):
  for root, dirs, files in os.walk(dirname):
    for filename in files:
      print(os.path.join(root, filename))
    for dir_name in dirs:
      walk2(dir_name)
      
