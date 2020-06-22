# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name=input('Enter the file name:')
hand=open(name)
dict=dict()
for line in hand:
    if not line.startswith('From'):
        continue
    else:
        line=line.split()
        line=line[5]
        line=line[0:2]
        dict[line]=dict.get(line,0)+1
lst=list()
for time,count in d.items():
    lst.append((time,count))

lst.sort()
for time,count in lst:
    print(time,count)
