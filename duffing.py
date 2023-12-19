import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from numpy import linspace
def harmonic():
    def f(x):
        return .5*(x**2)
    x=np.linspace(-5,5,1000)
    y=f(x)
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Harmonic Oscillator Potential")
    fig.savefig("harmonic potential")
def non_sym():
    def f(x):
        return (.5*(x**2))+(.167*(x**3))

    x = np.linspace(-4, 2.5, 1000)
    y = f(x)
    def g(x):
        x=x
        return (x*0)+0.7
    y2=g(x)
    fig, ax = plt.subplots()
    ax.plot(x, y,label="Potential")
    ax.plot(x, y2, label="Max Energy")
    ax.set_title("Non-Symmetric Potential")
    plt.legend()
    fig.savefig("Non-Symmetric Potential")
def duffing():
    def f(x):
        return (.5*(x**2))+(.25*(x**4))

    x = linspace(-3, 3, 1000)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y,label="Potential")
    ax.set_title("Duffing Potential")
    plt.legend()
    fig.savefig("Duffing Potential")
def solve_Duffing(w,e):
    def solvr(Y, t):
        return [Y[1], -w * Y[0] - e*(Y[0]**3)]
    t = np.linspace(0,7,1000)
    asol = integrate.odeint(solvr, [1, 0], t)
    x=t
    y=asol[:,0]
    return [x,y]
def plot_duffsol(w):
    e=0
    y_list=[]
    for counter in range(3):
        vals=solve_Duffing(w,e)
        x=vals[0]
        y=vals[1]
        y_list.append(y)
        e+=0.25
    fig, ax = plt.subplots()
    y=y_list[0]
    y2=y_list[1]
    y3=y_list[2]
    E=0.25
    pert_ylist=[]
    for counter in range(2):
        pert_y=pertval(w,E)
        pert_ylist.append(pert_y)
        E+=0.25
    x1 = np.linspace(0, 7, 1000)
    y4=pert_ylist[0]
    y5 = pert_ylist[1]
    ax.plot(x, y, label="zero epsilon-linear oscillator")
    ax.plot(x, y2, label="e=0.25")
    ax.plot(x, y3, label="e=0.5")
    ax.plot(x1, y4, label="perturbed e=0.25")
    ax.plot(x1, y5, label="perturbed e=0.5")

    ax.set_title("Numerical vs Perturbative Solution, omega squared=.25")
    plt.legend()
    fig.savefig("Numerical Solutions superlowagain")
def pertval(w,e):
    w=(w**.5)
    arg=w+(3*e/(8*w))
    amp=e/(32*(w**2))
    print("arg=",arg,"amp=",amp)
    def f(x):
        return ((1-amp)*np.cos(arg*x))+(amp*np.cos(3*arg*x))

    x1 = np.linspace(0, 7, 1000)
    y = f(x1)
    return(y)


plot_duffsol(.25)




