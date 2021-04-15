fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for a in line.split():
        #prints eack word
        if not a in lst:
            #add words to list if not there
            lst.append(a)
#print(lst)
lst.sort()
print(lst)
