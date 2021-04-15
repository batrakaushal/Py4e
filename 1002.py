fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
a=[]
for line in fh:
    if line.startswith("From "):
        list=line.split()
        #print(list)
        a.append(list[5])
#print(a)
hrs=[]
for h in a:
    hr=h.split(':')
    #print(hr)
    hrs.append(hr[0])
#print(hrs)
count = dict()
for hours in hrs :
    count[hours]=count.get(hours,0)+1
#print(count)
sort=dict()
sort=sorted(count.items())
#print(sort)
for a,b in sort:
    print(a,b)
