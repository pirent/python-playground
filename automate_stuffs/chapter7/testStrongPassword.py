#!/usr/bin/python3
import isStrongPassword as s

passwd = input('Enter your password: ')
print("Is your password strong enough? {}".format(s.isPasswordStrong(passwd))) 
