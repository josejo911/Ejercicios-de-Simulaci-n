'''
Mini Proyecto 2

Javier Jo 14343
Pablo Lopez 14509

'''

import numpy as np

def v(dist, N):
    print (sum(dist))
    if(sum(dist) != 1.0):
        print ("Suma de probabilidades no es 1")
    else: 
        print ("Suma de probabilidades es 1")
        interval = []
        #genero el intervalo
        for u in dist:
            if len(interval) != 0:
                interval.append(u+interval[-1])
            else:
                interval.append(u)
        x = np.random.random(N)
        c = [0]*len(interval) # aciertos del intervalo
        for xn in x:
            for i in range(0,len(interval)):
                if xn < interval[i] and xn > interval[i-1]:
                    #print "C "+str(i)+" +1 con el valor "+ str(xn)
                    c[i]+=1
                if i == 0 and xn < interval[0]:
                    #print "C "+str(i)+" +1 con el valor "+ str(xn)
                    c[i]+=1
        #imprimo mis aciertos
        for j in range(len(c)):
            percent = float(c[j])/N*100
            aster = "*" * int(percent/2)
            print (aster + " ("+str(c[j])+", %"+ str(percent)+")")
            
dist = [0.3, 0.15, 0.3, 0.2, 0.025, 0.025]
v(dist, 100000)

