# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname=input('Enter the file name:')
fname=open(fname)
lst=list()
for line in fname:
    if not line.startswith('From:'):
        continue
    line=line.split()
    lst.append(line[1])
counts=dict()
for word in lst:
    counts[word]=counts.get(word,0)+1
bigcount=0
bigword=0
for word,count in counts.items():
    if bigcount=None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword, bigcount)
