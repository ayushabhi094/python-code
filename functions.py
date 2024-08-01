def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)


a = 9
b = 81
if a>b:
    print("first no is greater")
else:
    print("second no is greater")
calculateGmean(a,b)