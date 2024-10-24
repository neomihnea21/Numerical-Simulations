#simulam o generalizare a problemei Monty Hall
import numpy as np
door_number=5
game_runs=100000
def run_game_2(doors): #cand se lasa 2 usi
    l=[i for i in range(1, door_number+1)]
    ferrari=np.random.choice(l)
    first_choice=np.random.choice(l)
    if(ferrari==first_choice): #daca ar castiga sa nu schimbi, cazul cu n-2 usi deschise
       return 0
    else: #invers, daca ar castiga sa schimbi
        return 1
def run_game(door, open):
    l=[i for i in range(1, door+1)]
    ferrari=np.random.choice(list(l))
    first_choice=np.random.choice(list(l))
    removed=0
    pos=set()
    i=0
    while(removed<open):
        if(l[i]!=ferrari and l[i] != first_choice):
            pos.add(l[i])
            removed+=1
        i+=1
    l2=[x for x in l if x not in pos]
    if(first_choice in l2):
       l2.remove(first_choice)
    #testam probabilitatea la schimbare
    new_choice=np.random.choice(l2)
    if(new_choice==ferrari):
        return 1
    else:
        return 0
wins=0
for i in range(game_runs):
    wins+=run_game(4, 2) # testul e facut cu 4 usi din care deschidem 2
print(wins)
