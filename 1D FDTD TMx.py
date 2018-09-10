# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:10:45 2018

@author: Cliente

FDTD 1D EX HY
TMx
"""
#import numpy as np
from matplotlib import pyplot as plt
from math import sin,pi,sqrt

ex = []
hy = []

cluz = 2.99792458e10
eps0 = (1.e-9)/(36*pi)
ami0 = (4.e-7)*pi
nx = 201
nt = 1000
f0 = 100e6
fs = f0/100
lamb= cluz/f0
dx = lamb/80
dt = 0.8/(cluz*sqrt(1/dx**2))
dt = 0.8*(dx/cluz)
isource = int((nx+1)/2)
vet_x = list(range(0,nx))

def savequad(quad,vet_x,campo):
    namequad = "quad" +  str(quad)
    plt.xlabel("X")
    plt.ylabel("Ex")
    plt.clf()
    plt.plot(vet_x,campo) #mandar listas para definir os eixos
    plt.savefig(namequad)

for i in range(0,nx):
    ex.append(0)
    hy.append(0)

for n in range(0,nt):
    for i in range(1,nx):
        ex[i] = ex[i] + (dt/eps0)*(hy[i-1]-hy[i])/dx
    ex[0] = 0     #PEC
    ex[nx-1] = 0  #PEC
    pulse = sin(2*pi*fs*n*dt)
    ex[isource] = pulse
    print (n,ex[isource+10])
    savequad(n,vet_x,ex)
    for i in range(0,nx-1):
        hy[i] =  hy[i] + (dt/ami0)*(ex[i] - ex[i+1])/dx
    
    
    
    