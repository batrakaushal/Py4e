fname= input("Enter name :")
file=open(fname)
lnum= list()
import re
for line in file:
    num=re.findall('[0-9]+',line)
    lnum=lnum+num
#print(lnum)
lst=list()
for i in range(0,len(lnum)):
    lst.append(int(lnum[i]))
#print(lst)
total=sum(lst)
print(total)
