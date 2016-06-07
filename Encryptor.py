#!/usr/bin/python
import datetime
import os
import string #fixed typo was using
rot7 = string.maketrans(
	    "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDabcdefghijklmnopqrstuvwxyz",
    	"GHIJKLABCDEFSTUVWXMNOPQRZYGHIJghijklabcdefstuvwxmnopqrzy")
userinput = raw_input("Give Code Here: ")
ciphertext = string.translate(userinput, rot7)
print ciphertext
