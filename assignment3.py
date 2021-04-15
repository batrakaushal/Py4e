hrs = input("Enter Hours:")
hrs = float(hrs)
rate =10.50
#rate after 40 hours
newrate=10.50*1.5
#pay is the total amount to be paid
if hrs<= 40.00:
    pay=float(rate)*float(hrs)
    print(pay)
elif hrs>40:
    #extra hours need to be calculated
    ehours=hrs-40
    pay=(40*10.50)+(float(ehours)*float(newrate))
    print(pay)
