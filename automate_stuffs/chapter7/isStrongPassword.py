#!/usr/bin/python3
# uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit
import re

pwdRegex = re.compile(r'''(
  ^(?=.*[A-Z].*)	# uppercase characters
   (?=.*[a-z].*)	# lowercase characters
   (?=.*\d+.*)		# at least one digit
   .{8,}		# al least eight characters long
)''', re.VERBOSE)

def isPasswordStrong(password):
  mo = pwdRegex.search(password)
  return mo is not None
