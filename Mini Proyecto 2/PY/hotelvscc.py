'''
Mini Proyecto 2

Javier Jo 14343
Pablo Lopez 14509

'''

import math
import random

#def exponential
def e(lam):
    return -(1/lam)*math.log(random.random(),math.exp(1))
    
def normal(M,sigma):
    while True:
        y1 = e(1)
        y2 = e(1)
        if (y2 - (y1-1)**2)/2 > 0:
            y = (y2 - (y1-1)**2)/2
            u = random.random()
            if u <= 0.5:
                return M + sigma*y1
            else:
                return M - sigma*y1
#def uniform
def uniform(a,b):
    x = random.random()
    # a y b rango que nos dan
    r = (b-a)*x+a
    return r  
#def value present net
def valuePN(V,t):
    r = 0
    for i in range(0,len(V)):
        r += V[i]/((1+t)**i)
    return r

print ("Ejercicio 3")
print ("Simulación con 100 Iteraciones")
t = 0.1 #rate
iteraciones = 100
p_hotel,p_cc = 0,0
for i in range(iteraciones):
    #init hotel y centro comercial con las dist
    hotel = [-800, normal(-800,50), normal(-800,100), normal(-700,150), normal(300,200), normal(400,200), normal(500,200), uniform(200,8440)]
    cc = [-900, normal(-600,50), normal(-200,50), normal(-600,100), normal(250,150), normal(350,150), normal(400,150), uniform(1600,6000)]
    #sumamos el valor esperado neto
    p_hotel += valuePN(hotel,t)
    p_cc += valuePN(cc,t)
print ("Promedio de Valor Presente Neto en la inversión del proyecto del Hotel: " + str(p_hotel/iteraciones))
print ("Promedio de Valor Presente Neto en la inversión del proyecto del Centro Comercial: " + str(p_cc/iteraciones))
if p_hotel < p_cc:
    print ("El proyecto mas rentable es el Centro Comercial.")
else:
    print ("El proyecto mas rentable es el Hotel.")

print ("Simulación con 1000 Iteraciones")
t = 0.1
iteraciones = 1000
p_hotel,p_cc = 0,0
for i in range(iteraciones):
    #init hotel y centro comercial con las dist
    hotel = [-800, normal(-800,50), normal(-800,100), normal(-700,150), normal(300,200), normal(400,200), normal(500,200), uniform(200,8440)]
    cc = [-900, normal(-600,50), normal(-200,50), normal(-600,100), normal(250,150), normal(350,150), normal(400,150), uniform(1600,6000)]
    #sumamos el valor esperado neto
    p_hotel += valuePN(hotel,t)
    p_cc += valuePN(cc,t)
print ("Promedio de Valor Presente Neto en la inversión del proyecto del Hotel: " + str(p_hotel/iteraciones))
print ("Promedio de Valor Presente Neto en la inversión del proyecto del Centro Comercial: " + str(p_cc/iteraciones))
if p_hotel < p_cc:
    print ("El proyecto mas rentable es el Centro Comercial.")
else:
    print ("El proyecto mas rentable es el Hotel.")


print ("Simulación con 10000 Iteraciones")
t = 0.1
iteraciones = 10000
p_hotel,p_cc = 0,0
for i in range(iteraciones):
    #init hotel y centro comercial con las dist
    hotel = [-800, normal(-800,50), normal(-800,100), normal(-700,150), normal(300,200), normal(400,200), normal(500,200), uniform(200,8440)]
    cc = [-900, normal(-600,50), normal(-200,50), normal(-600,100), normal(250,150), normal(350,150), normal(400,150), uniform(1600,6000)]
    #sumamos el valor esperado neto    
    p_hotel += valuePN(hotel,t)
    p_cc += valuePN(cc,t)
print ("Promedio de Valor Presente Neto en la inversión del proyecto del Hotel: " + str(p_hotel/iteraciones))
print ("Promedio de Valor Presente Neto en la inversión del proyecto del Centro Comercial: " + str(p_cc/iteraciones))
if p_hotel < p_cc:
    print ("El proyecto mas rentable es el Centro Comercial.")
else:
    print ("El proyecto mas rentable es el Hotel.")