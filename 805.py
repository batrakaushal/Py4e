fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
a=[]
for line in fh:
    if line.startswith("From:"):
        list=line.split()
        a=a+list
