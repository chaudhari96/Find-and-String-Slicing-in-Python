# Find-and-String-Slicing-in-Python
Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
Line : X-DSPAM-Confidence:    0.8475


Code:
text = "X-DSPAM-Confidence:    0.8475";                     # variable assigned
ntext = text.find(':')                                      # use of 'variable.find()' to find ':' in text
host=text[ntext+1:]                                         # this line states that the new variable host should start one character after ntext 
ftext=float(host)                                           # converting the host file 
print(ftext)
