import numpy as np
import matplotlib.pyplot as plt
import time
#Simulare vectorizata pentru aruncari  cu banul
def simulate_coin_tosses(n, prob_cap):
    start=time.perf_counter()
    heads=0
    tails=0
    x=[]
    y=[]
    for i in range(n):
        rd=np.random.random()
        if(rd<prob_cap):
            heads+=1
        else:
            tails+=1
        x.append(heads/(heads+tails))
        y.append(i)
    end=time.perf_counter()
    timp=end-start
    print("A durat clasic: "+str(timp)) 
    plt.plot(y, x)
    plt.axhline(0.5, linestyle='--', color='red')
    plt.show()
    return heads
# acum sa facem asta cu SIMD
def vectorised_coin_toss(n):
    start=time.perf_counter()
    toss=np.random.random(n)
    c=np.sum(toss<0.5)
    end=time.perf_counter()
    print("A durat cu SIMD: "+str(end-start))
    return c.sum()
def simulate_die(n):
    a=[0 for i in range(7)]
    for i in range(n):
        rd=np.random.random()
        a[np.floor(1+6*rd)]+=1
def game_of_biased_dice(d1, d2):
    win=0
    loss=0
    draw=0
    for i in range(6):
        for j in range(6):
            if(d1[i]<d2[j]):
                win+=1
            elif(d1[i]>d2[j]):
                loss+=1
            else:
                draw+=1
numar_incercari=1000000
print(vectorised_coin_toss(numar_incercari))
print(simulate_coin_tosses(numar_incercari, 0.5))
