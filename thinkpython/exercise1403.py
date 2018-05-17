# =========================================================
# Write a program that searches a directory and all of its subdirectories, recursively, and returns
# a list of complete paths for all files with a given suffix (like .mp3 )
#
# To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two
# files have the same checksum, they probably have the same contents.
# =========================================================
import os

# mapping md5 and files who have the same
mapping = {}
cmd = 'md5sum'

def collect_files_and_theirs_md5(dirname, file_suffix):
  for path, dirs, files in os.walk(dirname):
    for filename in files:
      if not filename.endswith(file_suffix):
        continue
 
      filepath = os.path.join(path, filename)
      md5sum = calculate_md5sum(filepath)
     
      if md5sum in mapping:
        mapping[md5sum].append(filepath)
      else:
        mapping[md5sum] = [filepath]
    for dir_name in dirs:
      collect_files_and_theirs_md5(dir_name, file_suffix)

def calculate_md5sum(filepath):
  fp = os.popen(cmd + " " + filepath)
  res = fp.readline()
  fp.close()
  return res.split()[0]

def find_duplicated_files():
  res = []
  for md5sum, files in mapping.items():
    if len(files) > 1:
      res.append(files)
  return res

if __name__ == "__main__":
  collect_files_and_theirs_md5('/tmp/music', '.mp3')
  #print(">> DEBUG: after collecting:", mapping)

  duplicated_files = find_duplicated_files() 
  print("Duplicated files are:")
  for df in duplicated_files:
    print(df)
