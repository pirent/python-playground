#!/usr/bin/python3
# find phone number for a given string
import re

phoneNumberRegex = re.compile(r'(\(\d{3}\)-)?(\d{3}-\d{4})')

mo = phoneNumberRegex.search('My number is (415)-555-4242')
areaCode, mainNumber = mo.groups()
print('Phone number found: ' + mo.group(0))
print('Area code: {}, main number: {}'.format(areaCode, mainNumber))
print('===================================')
print('Mo group 1: ' + mo.group(1))
print('Mo group 2: ' + mo.group(2))
print('Mo group 0: ' + mo.group(0))
print('Mo group without specifying number: ' + mo.group())

mo2 = phoneNumberRegex.search('My number is 555-4242')
print(mo2.group())
