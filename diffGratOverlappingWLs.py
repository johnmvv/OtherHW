import math
import matplotlib.pyplot as plt
import random
#n1 is an integer
#n2 is an integer
#l1 < 3300/n1
#l2 < 3300/n2
#360 < l1 < 750
#360 < l2 < 750
#l1 != l2
#n1 != n2
#n1*l1 = n2*l2 = 300*sin(theta)
#theta = 0 to 90
#n1 < 10
#n2 < 10

l1s = []
l2s = []
n1s = []
n2s = []
thetas = []

for n1 in range(1,9):
    for n2 in range(n1,9):
        for l1 in range(360,750):
            if(n1*l1)/3334 > 1:
                continue
            l2 = (n1*l1)/n2
            if l1 > 3333/n1:
                continue
            if l2 > 3333/n2:
                continue
            if l2 < 360 or l2 > 750:
                continue
            if l1 == l2:
                continue
            if l1 in l1s and l2 in l2s:
                continue
            l1s.append(l1)
            l2s.append(l2)
            n1s.append(n1)
            n2s.append(n2)
            thetas.append(math.asin((n1*l1)/3333))
            print("l1: ", l1, "l2: ", l2, "theta: ", math.asin((n1*l1)/3333))

thetasInDegrees = []
cols = [[1,0,0], [0,1,0], [0,0,1]]
colcount = 0
for theta in thetas:
    thetasInDegrees.append(math.degrees(theta))

colours = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
for i in range (len(thetasInDegrees)):
    if l1s[i] < 450:
        plt.scatter(thetasInDegrees[i],l1s[i], color=colours[0])
    elif l1s[i] < 500:
        plt.scatter(thetasInDegrees[i],l1s[i], color=colours[1])
    elif l1s[i] < 565:
        plt.scatter(thetasInDegrees[i],l1s[i], color=colours[2])
    elif l1s[i] < 590:
        plt.scatter(thetasInDegrees[i],l1s[i], color=colours[3])
    elif l1s[i] < 625:
        plt.scatter(thetasInDegrees[i],l1s[i], color=colours[4])
    else:
        plt.scatter(thetasInDegrees[i],l1s[i], color=colours[5])
for i in range (len(thetasInDegrees)):
    if l2s[i] < 450:
        plt.scatter(thetasInDegrees[i],l2s[i], color=colours[0])
    elif l2s[i] < 500:
        plt.scatter(thetasInDegrees[i],l2s[i], color=colours[1])
    elif l2s[i] < 565:
        plt.scatter(thetasInDegrees[i],l2s[i], color=colours[2])
    elif l2s[i] < 590:
        plt.scatter(thetasInDegrees[i],l2s[i], color=colours[3])
    elif l2s[i] < 625:
        plt.scatter(thetasInDegrees[i],l2s[i], color=colours[4])
    else:
        plt.scatter(thetasInDegrees[i],l2s[i], color=colours[5])


#plt.scatter(thetasInDegrees,l1s, color='red')
#plt.scatter(thetasInDegrees,l2s, color='blue')
#for i in range(len(thetasInDegrees)):
#    print("n1: ", n1s[i], "n2: ", n2s[i], "l1: ", l1s[i], "l2: ", l2s[i], "theta: ", thetasInDegrees[i])
#    plt.plot([thetasInDegrees[i],thetasInDegrees[i]],[l1s[i],l2s[i]],color=cols[colcount])
#    if i != len(thetasInDegrees)-1:
#        if (l1s[i] - l1s[i+1]) > 0:
#            if colcount < 2:
#                colcount += 1
#            else:
#                colcount = 0
#
plt.show()
