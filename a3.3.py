score = input("Enter Score: ")
try :
    s=float(score)
except:
    print("enter a valid score between 0.0 to 1.0")
    quit()
if s>1:
    print("Enter a Valid score between 0.0 to 1.0")
    quit()
if s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
elif s<0.6:
    print("F")
