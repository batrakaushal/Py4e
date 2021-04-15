text = "X-DSPAM-Confidence:    0.8475"
ipos=text.find(':')
print(text.find(':'))
number=text[ipos:]
print(float(number.strip()))
