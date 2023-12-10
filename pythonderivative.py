# Leo Berman Derivative

import numpy as np
import scipy.fft as sc
import sympy as sp
t = sp.symbols('t')
w = sp.symbols('w')



A = 30
a = 5
f = A*sp.exp(-a*t)*sp.exp(1j*w*t)
fpiece = sp.Piecewise((0,t<0),(f,t>=0))

f_ft = sp.fourier_transform(f*sp.Heaviside(t), t, w)
print(f_ft)

'''x = sp.symbols('x')

y = ((2*x-3)**4)*((x**2+x+1)**5)
dydx = y.diff(x)
print(dydx)

def y(t):
    return (.5*(t+4)*np.heaviside(t+4,0))-(.5*(t+2)*np.heaviside(t+2,0))-(.5*(t+1)*np.heaviside(t+1,0)) + (.5*(t-1)*np.heaviside(t-1,0))+(.5*(t-2)*np.heaviside(t-2,0))-(.5*(t-4)*np.heaviside(t-4,0))-(.5*(t-5)*np.heaviside(t-5,0))+(.5*(t-7)*np.heaviside(t-7,0))

def x(t):
    return np.heaviside(t+4,0)-np.heaviside(t+2,0)+np.heaviside(t-2,0)-np.heaviside(t-4,0)
t = np.linspace(-6,9,100)
plt.plot(t,x(t))
plt.plot(t,y(t))
plt.show()

t=sp.symbols('t')
s=sp.symbols('s')
yt = (.5*(t+4)*sp.Heaviside(t+4))-(.5*(t+2)*sp.Heaviside(t+2))-(.5*(t+1)*sp.Heaviside(t+1)) + (.5*(t-1)*sp.Heaviside(t-1))+(.5*(t-2)*sp.Heaviside(t-2))-(.5*(t-4)*sp.Heaviside(t-4))-(.5*(t-5)*sp.Heaviside(t-5))+(.5*(t-7)*sp.Heaviside(t-7))
xt = sp.Heaviside(t+4)-sp.Heaviside(t+2)+sp.Heaviside(t-2)-sp.Heaviside(t-4)
Xs = sp.laplace_transform(xt,t,s,noconds=True)
#print("Xs = ",Xs)
Ys = sp.laplace_transform(yt,t,s,noconds=True)
#print("Ys = ",Ys)
Hs = Ys/Xs
#print("Hs = ",Hs)
ht = sp.inverse_laplace_transform(Hs.apart(),s,t,noconds=True)*sp.Heaviside(t)
print("ht = ",ht)
sp.plot(ht)'''