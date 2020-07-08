import random
from math import sqrt
from matplotlib import pyplot as plt

def mean(x):

    xTotal = 0
    for num in x:
        xTotal += num
    xLen = len(x)
    xMean=xTotal/xLen
    return xMean

def sumSig(num, mean):
    newLis = []
    for n in num:
        newLis.append(n - mean)
    return newLis
def main():
    # Generate random plots on the graph
    x = range(50)
    y = []
    for num in x:
        add = random.randrange(-5, 5)
        y.append(num+ add)
    plt.scatter(x, y)
    plt.show()

    xSig = (sumSig(x, mean(x)))
    ySig = (sumSig(y, mean(y)))
    totSig= sum([xEle*yEle for xEle,yEle in zip((xSig),(ySig))]) # E((x-mean)(y-mean))
    sumXsqu = sum([xEle**2 for xEle in xSig])
    sumYsqu = sum([yEle**2 for yEle in ySig])
    r = totSig/(sqrt(int((sumXsqu)*(sumYsqu))))
    slope = r*(sumYsqu/sumXsqu)
    xInter = mean(y)- (slope*mean(x))
    y = []
    for i in x:
        y.append(xInter + (slope*i))
    plt.plot(x, y)
    plt.show()
    print("well")
    print(xInter)
    print(slope)
    xnum = float(input())

    print(xInter + (slope*xnum))


main()
