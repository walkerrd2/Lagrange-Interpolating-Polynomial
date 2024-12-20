import numpy as np
import matplotlib.pyplot as plt

def davis_lagrange(xvalue, xdata, ydata):
    P = 0
    n = xdata.size
    for k in range(0,n):
        L = 1
        for i in range (0,n):
            if (i != k):
                L=L*(xvalue-xdata[i])/(xdata[k]-xdata[i])
        P = P + ydata[k]*L
    return P

x1 = np.array([0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3, 2*np.pi])
y1 = np.array([0, (3**0.5)/2, (3**0.5)/2, 0, -(3**0.5)/2,-(3**0.5)/2,0])

# Approximating sin(pi/8)
p1 = davis_lagrange(np.pi/8, x1, y1)
print(p1)

# Calculating relative error with np.sin(np.pi/8) as exact value
absolerr = np.abs(p1 - np.sin(np.pi/8)) #creating absolute error handle
print("Relative error = {}".format(np.abs(absolerr/np.sin(np.pi/8))))


xvals = np.linspace(0, 2*np.pi, 100)
yvals1 = davis_lagrange(xvals,x1,y1)
yexact = np.sin(xvals)

plt.plot(xvals,yvals1, 'r-', label='Approximation')
plt.plot(xvals,yexact,'c^', label='Exact')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Lagrange Interpolating')
plt.xlim(0,2*np.pi)
plt.ylim(-1,1)
plt.legend()
plt.grid()
plt.show()
