import numpy as np
import matplotlib.pyplot as plt


#x = np.linspace(0,314, num=5)
#x = np.linspace(0,314, num=13)
x = np.linspace(0,314, num=25)
#x = np.linspace(0,314, num=314)

y = np.sin(x*0.02)


#for i in x:
#    print(x, y)
#print(y)

print()

listx = list(x)
listy = list(y*100)

print()

print('x =', listx)
print('y =', listy)

print()

print(int(x[0]), ' -- ', y[0])
print(int(x[1]), ' -- ', y[1])
print(int(x[2]), ' -- ', y[2])
print(int(x[3]), ' -- ', y[3])
print(int(x[4]), ' -- ', y[4])
print(int(x[5]), ' -- ', y[5])
print(int(x[6]), ' -- ', y[6])

print()
#print(int(y))
print( 'X', x)
print( 'Y', y)
print( 'X + Y pos 1 ---', int(x[1]), 'x To ', y[1]*100, 'y')



plt.figure(num=0,dpi=90)
plt.plot(x,y, linewidth = 3)

plt.xlabel('Cir (x)', fontweight = 'bold', fontsize = 12)
plt.ylabel(r'Diameter (y)', fontweight = 'bold', fontsize = 12)
plt.title('Elbow', fontweight = 'bold', fontsize = 14)
#plt.grid(True)
plt.show()
