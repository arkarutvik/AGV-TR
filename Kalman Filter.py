import numpy as np
import matplotlib.pyplot as plt

path = "/Users/Arka Rutvik/Downloads/kalmann.txt"
file = open(path,'r')
i=0
while(file.readline() != ''):
    i = i+1

print(i)
p1= 0.00000000001 * np.eye(2,dtype = np.uint8)
I = np.eye(2,dtype = np.uint8)
r = 0.000000000001*I
q = I
q = q
lx = []
ly =[]
j=0
i=0
file = open(path,'r')
f = file.readline()
k=0
n=-1
list = []
m = np.array([372.99815102559614,3.686804471625727])
while(k<359):
    file= open(path,'r')
    g=0
    while(g<k):
        file.readline()
        g = g+1
    f = file.readline()
    for i in f:
        j=j+1
        if i == ',':
            list.append(f[n+1:j-1])
            n=j
    list.append(f[n+1:])
    x = float(list[0])
    y = float(list[1])
    dist = np.array([x,y]).reshape((2,1))
    list = []
    j=0
    n=-1
    a = file.readline()
    for i in a:
        j=j+1
        if i == ',':
            list.append(a[n+1:j-1])
            n=j
    list.append(a[n+1:])
    c = float(list[0])
    d = float(list[1])
    p = float(list[2])
    q = float(list[3])
    list = []
    j=0
    m = np.array([c,d]).reshape((2,1))
    vel = np.array([p,q]).reshape((2,1))
    dist = dist + vel
    p0 = p1 + q
    kal = np.dot(p0,np.linalg.inv(p0+r))
    fin = dist + np.dot(kal,(m-dist))
    fin = fin.reshape((1,2))
    lx.append(fin[0][0])
    ly.append(fin[0][1])
    p1 = np.dot((I-kal),p0)
    k = k+1
    j=0
    n = -1
    
    
plt.plot(lx,ly)
plt.show