
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Halima Elmi
# Date:09/16/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py


name="Halima"
str.upper(name)
age=18
print("How are you {}? Happy {} birthday!" . format(name,age))

#TO-DO 2:
# Create a variable called "words".
# The value of words should be "The quick brown fox jumps over the lazy dog".
words="The quick brown fox jumps pver the lazy dog"
# Use indexing to return the first and 17th charecters of "words" to the user.
print("The first character is, "words[0])
print("The 17th character is, "words[16])
words= "The quick brown fox jumps over the lazy dog"

#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.
slice1=words[-23:-18]
print(slice1)
slice2=words[-39:-34]
print(slice2)

#TO-DO 4:
# Use slicing to retun everything between index 2-15 to the user.
slice3=words[2:15]
print(slice3)
print(words[5:22])
# Print "uick brown foxs ju" from "words".
print(words[5:22])

