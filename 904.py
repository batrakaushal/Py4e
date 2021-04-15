fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
a=[]
for line in fh:
    if line.startswith("From:"):
        list=line.split()
        a.append(list[1])
#print(a)
count=dict()
for mail in a:
    count[mail]=count.get(mail,0)+1
#print(count)
email = None
number=None
for mails,counts in count.items():
    if email is None or counts > count[mail]:
        email=mail
        number=count[mail]
print(email,number)
