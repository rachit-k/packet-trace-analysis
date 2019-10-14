import csv 
from matplotlib import pyplot as plt
import numpy as np
from array import array

f= open("temp.txt","w+")

l=0.1*np.arange(2800)
s=list()
w=list()
for i in l:
	s.append(i/(286-i))
	w.append(i/((286-i)*(286)))
x=array("f",s)
y=array("f",w)
plt.plot(l,x)
plt.ylabel('queue size')
plt.xlabel('lambda')
plt.show()		
plt.plot(l,y)
plt.ylabel('waiting time')
plt.xlabel('lambda')
plt.show()	