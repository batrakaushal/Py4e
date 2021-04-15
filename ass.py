def computepay(h,r):
    if h<=40:
        pay=(float(h)*float(r))
        return pay
    elif h>40:
        pay=(40*float(r))+(float(h-40)*float(1.5*r))
        return pay

hrs = input("Enter Hours:")
#Hours
hours=float(hrs)
#rate
rate= input("Enter Rate: ")
rate=float(rate)
p = computepay(hours,rate)
print("Pay",p)
