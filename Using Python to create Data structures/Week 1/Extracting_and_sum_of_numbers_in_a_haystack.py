# Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_704620.txt (There are 89 values and the sum ends with 773) : 'File named as a.txt in the code'

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

#Code:


import re
hand = open("a.txt")
lst = list()

for line in hand:
    line = line.rstrip()
    numbers = re.findall("([0-9]+)", line)


    for i in range(len(numbers)):
        num = float(numbers[i])
        lst.append(num)

print(sum(lst))
