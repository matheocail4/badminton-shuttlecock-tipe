import os
import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt

# Les donnees de pointage (Tracker) sont dans le dossier data/
DONNEES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

#VOLANT À PLUMES
#Étude expérimentale

fichier = open(os.path.join(DONNEES, 'feather.txt'), 'r', encoding='utf-8')
traj = fichier.readlines()
fichier.close()
traj.pop(0)

lx = []
ly = []
for ligne in traj:
    m = str(ligne).replace(",", ".")
    for i in range(len(list(m))):
        if list(m)[i] == '\t':
            m = m[:i]+ ";" +m[i+1:]
    don = m.strip().split(';')
    lx.append(float(don[1]))
    ly.append(float(don[2]))

h = ly[-1]
for k in range(len(ly)):
    ly[k] -= h

#Étude théorique
#Données
a = 40.3*np.pi/180
v0 = 24.2
g = 9.8
vl = 4.71
P = vl*v0*np.cos(a)/g # P correspond à la valeur limite: ie lorsqu'il y a une asymptote verticale

#Équation du mouvement pour frottement linéaire
def y(x):
    return np.tan(a)*x - 0.5*g*(vl*np.log(1-g*x/(vl*v0*np.cos(a)))/g)**2 - h

#Recherche du point de chute
def dichotomie(f, a, b, epsilon):
    m = (a + b)/2.
    while abs(a - b) > epsilon:
        if f(m) == 0.:
                return m
        elif f(a)*f(m) > 0:
            a = m
        else:
            b = m
        m = (a + b)/2
    return m

C = dichotomie(y, 0, P, 0.001)

#Modélisation graphique
plt.plot(lx, ly, color='blue', label='Expérimental')

dist = np.linspace(0, C, 100)
traj = [y(x) for x in dist]
plt.plot(dist, traj, color='green', label='Théorique : frottement linéaire')

plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparaison expérimental/théorique pour un volant à plume')
plt.xlim(0)
plt.ylim(0)
plt.grid()
plt.show()

print("Différence point de chute théorique/expérimentale :", round(abs(C-lx[-1]), 2), 'm')

#Détermination de l'équation avec un frottement quadratique
def eqfr(mobile, dist):
    A = (0.5*0.57*1.2*np.pi*0.035**2)/0.004
    x, y, dx, dy = mobile
    v = np.sqrt(dx**2 + dy**2)
    return [dx, dy, -A*v*dx, -g-A*v*dy]

dist = np.linspace(0, P, 1000)
x, y, vx, vy = sp.odeint(eqfr, (0, -h, v0*np.cos(a), v0*np.sin(a)), dist).T

y = [k for k in y if k>0]
x = x[:len(y)]

#Modélisation graphique avec ordre 2
plt.plot(x, y, color='red', label='Théorique : frottement quadratique')
plt.plot(lx, ly, color='blue', label='Expérimental')

plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparaison expérimental/théorique pour un volant à plume')
plt.xlim(0)
plt.ylim(0)
plt.grid()
plt.show()

print("Différence point de chute théorique/expérimentale :", round(abs(x[-1]-lx[-1]), 2), 'm')

#VOLANT EN PLASTIQUE
#Étude expérimentale

fichier = open(os.path.join(DONNEES, 'plastic.txt'), 'r', encoding='utf-8')
traj = fichier.readlines()
fichier.close()
traj.pop(0)

lx = []
ly = []
for ligne in traj:
    m = str(ligne).replace(",", ".")
    for i in range(len(list(m))):
        if list(m)[i] == '\t':
            m = m[:i]+ ";" +m[i+1:]
    don = m.strip().split(';')
    lx.append(float(don[1]))
    ly.append(float(don[2]))

h = ly[-1]
for k in range(len(ly)):
    ly[k] -= h

#Étude théorique
#Données
a = 25.4*np.pi/180
v0 = 15
g = 9.8
vl = 8.16
P = vl*v0*np.cos(a)/g # P correspond à la valeur limite: ie lorsqu'il y a une asymptote verticale

#Équation du mouvement pour frottement linéaire
def y(x):
    return np.tan(a)*x - 0.5*g*(vl*np.log(1-g*x/(vl*v0*np.cos(a)))/g)**2 - h

#Recherche du point de chute
def dichotomie(f, a, b, epsilon):
    m = (a + b)/2.
    while abs(a - b) > epsilon:
        if f(m) == 0.:
                return m
        elif f(a)*f(m) > 0:
            a = m
        else:
            b = m
        m = (a + b)/2
    return m

C = dichotomie(y, 0, P, 0.001)

#Modélisation graphique
plt.plot(lx, ly, color='blue', label='Expérimental')

dist = np.linspace(0, C, 100)
traj = [y(x) for x in dist]
plt.plot(dist, traj, color='green', label='Théorique : frottement linéaire')

plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparaison expérimental/théorique pour un volant en plastique')
plt.xlim(0)
plt.ylim(0)
plt.grid()
plt.show()

print("Différence point de chute théorique/expérimentale :", round(abs(C-lx[-1]), 2), 'm')

#Détermination de l'équation avec un frottement quadratique
def eqfr(mobile, dist):
    A = (0.5*0.57*1.2*np.pi*0.03**2)/0.005
    x, y, dx, dy = mobile
    v = np.sqrt(dx**2 + dy**2)
    return [dx, dy, -A*v*dx, -g-A*v*dy]

dist = np.linspace(0, P, 1000)
x, y, vx, vy = sp.odeint(eqfr, (0, -h, v0*np.cos(a), v0*np.sin(a)), dist).T

y = [k for k in y if k>0]
x = x[:len(y)]

#Modélisation graphique avec ordre 2
plt.plot(x, y, color='red', label='Théorique : frottement quadratique')
plt.plot(lx, ly, color='blue', label='Expérimental')

plt.legend(loc='best')
plt.xlabel('x en m')
plt.ylabel('y(x) en m')
plt.title('Comparaison expérimentale/théorique pour un volant en plastique')
plt.xlim(0)
plt.ylim(0)
plt.grid()

plt.show()

print("Différence point de chute théorique/expérimentale :", round(abs(x[-1]-lx[-1]), 2), 'm')

#OSCILLATIONS DU VOLANT
#Traitement des données de Tracker

fichier = open(os.path.join(DONNEES, 'oscillation_angles.txt'), 'r', encoding='utf-8')
traj = fichier.readlines()
fichier.close()
traj.pop(0)

lt = []
ltheta = []
for ligne in traj:
    b = str(ligne).replace(",", ".")
    m = b
    for i in range(len(list(b))):
        if list(b)[i] == '\t':
            m = m[:i]+ ";" +m[i+1:]
    don = m.strip().split(";")
    lt.append(float(don[0]))
    ltheta.append(float(don[1]))

#Résolution théorique
D= 957
C = 7.1
t = np.linspace(0,lt[-1],500)

def f(X,t):
    theta,thetapoint = X
    return thetapoint , -C*thetapoint - D*np.sin(theta)

def sol(theta0,thetapoint0):
    return sp.odeint(f,[theta0,thetapoint0],t)[:,0]

theta0=-np.pi
thetapoint0=50

plt.plot(t,180*(sol(theta0,theta0))/np.pi+360, color='green', label='Théorique')
plt.plot(lt, ltheta, color='blue', label='Expérimental')
plt.xlabel('Temps en s')
plt.ylabel('Angle en °')
plt.title('Oscillations du volant')
plt.grid()
plt.legend(loc='best')
plt.xlim(0)
plt.ylim(-180*abs(theta0)/np.pi)
plt.show()

#VOLANT DÉTÉRIORÉ
#Traitement des données de Tracker

fichier = open(os.path.join(DONNEES, 'damaged.txt'), 'r', encoding='utf-8')
traj = fichier.readlines()
fichier.close()
traj.pop(0)

lx = []
ly = []
for ligne in traj:
    m = str(ligne).replace(",", ".")
    for i in range(len(list(m))):
        if list(m)[i] == '\t':
            m = m[:i]+ ";" +m[i+1:]
    don = m.strip().split(';')
    lx.append(float(don[1]))
    ly.append(float(don[2]))

h = ly[-1]
for k in range(len(ly)):
    ly[k] -= h

plt.plot(lx, ly, color='blue', label='Expérimental')

#Données
a = 15*np.pi/180
v0 = 13
g = 9.8
vl = 9
P = vl*v0*np.cos(a)/g # P correspond à la valeur limite: ie lorsqu'il y a une asymptote verticale

#Équation du mouvement pour frottement linéaire
def y(x):
    return np.tan(a)*x - 0.5*g*(vl*np.log(1-g*x/(vl*v0*np.cos(a)))/g)**2 - h

#Recherche du point de chute
def dichotomie(f, a, b, epsilon):
    m = (a + b)/2.
    while abs(a - b) > epsilon:
        if f(m) == 0.:
                return m
        elif f(a)*f(m) > 0:
            a = m
        else:
            b = m
        m = (a + b)/2
    return m

C = dichotomie(y, 0, P, 0.001)

dist = np.linspace(0, C, 100)
traj1 = [y(x) for x in dist]
plt.plot(dist, traj1, color='green', label='Théorique : frottement linéaire')

#Détermination de l'équation avec un frottement quadratique
def eqfr(mobile, dist):
    A = (0.5*0.57*1.2*np.pi*0.035**2)/0.004
    x, y, dx, dy = mobile
    v = np.sqrt(dx**2 + dy**2)
    return [dx, dy, -A*v*dx, -g-A*v*dy]

dist = np.linspace(0, P, 1000)
x, y, vx, vy = sp.odeint(eqfr, (0, -h, v0*np.cos(a), v0*np.sin(a)), dist).T

y = [k for k in y if k>0]
x = x[:len(y)]

plt.plot(x, y, color='red', label='Théorique : frottement quadratique')

plt.legend(loc='best')
plt.xlabel('x en m')
plt.ylabel('y(x) en m')
plt.title('Comparaison expérimentale/théorique pour un volant à plumes détérioré')
plt.xlim(0)
plt.ylim(0)
plt.grid()

plt.show()

print("Différence point de chute théorique (linéaire) / expérimentale :", round(abs(C-lx[-1]), 2), 'm')
print("Différence point de chute théorique (quadratique) / expérimentale :", round(abs(x[-1]-lx[-1]), 2), 'm')