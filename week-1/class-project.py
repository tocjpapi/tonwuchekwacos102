#Simple Interest
p = 1000
r = 5
t = 2


si = (p * (1 + (r * t)/ 100))
print(si)

#Compound Interest
p = 1000
r = 5
t = 2
n = 2


ci = p * ((1 + (r / 100)) ** (n * t))
print(ci)

#Annuity Plan
pmt = 200
r = 5
t = 2
n = 12


ap = pmt * (-1  +(1 + r / n) ** (n * t)) / (r / n)
print(ap)
