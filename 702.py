# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
all=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
        ipos=line.find(':')
        value=line[ipos+1:]
        value=value.strip()
        value=float(value)
        all=all+value
        print(all)

    elif not line.startswith("X-DSPAM-Confidence:") :
        continue
print(count)
print(all)
average=(all/count)
print(average)
