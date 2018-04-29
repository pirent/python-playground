"""
  Return true only if the word contains only letters in the list
  Example: word='Hoe alfalfa', letters='acefhlo'
"""
def uses_only(word, letters):
  for letter in word:
    if not letter in letters and letter.isalpha():
      return False
  return True

if __name__ == "__main__":
  word = input("Enter word: ")
  letters = input("Enter string of letters: ")
  print("Is {} contains only {}? {}".format(word, letters, uses_only(word, letters)))
