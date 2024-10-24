

# 1a
print(62**8)
#1b
countSeconds=(62**8)/(10**6)
countYears=countSeconds/(86400*365)
print(str(countYears)+" ani")
#1c
failChance=1-(1/(62**8))
testsDone=(10**6)*86400*7
print(1-failChance**(testsDone))
#2
def fact(n):
    ans=1
    for i in range(1, n+1):
        ans*=i
    return ans
def aranjamente(n, k):
    return fact(n)/fact((n-k))
#2a
probabilitateDistinct=aranjamente(62, 8)
print(probabilitateDistinct)
#2b
print(probabilitateDistinct*52/62)
#3
def combinari(n, k):
    return fact(n)/(fact(n-k)*fact(k))
combo_virusi=combinari(10, 3)
print(combo_virusi)
#4
corect_laptopuri_bune=combinari(13, 3)
corect_laptopuri_proaste=combinari(7, 3)
print((corect_laptopuri_bune*corect_laptopuri_proaste)/combinari(20, 6))
max_prob=0
max_index=0
for i in range(0, 7):
    prob=combinari(13, i)*combinari(7, 6-i)/combinari(20, 6)
    if(prob>max_prob):
        max_prob=prob
        max_index=i
print("Cel mai des, vor fi "+str(6-max_index)+" proaste")
#5
numarAsi=combinari(4, 3)
numarRest=combinari(48, 2)
print(numarAsi*numarRest/combinari(52, 5))

max_prob=0
max_index=0
for i in range(0, 5):
    prob=combinari(4, i)*combinari(48, 5-i)/combinari(52, 5)
    if(prob>max_prob):
        max_prob=prob
        max_index=i
print("Cel mai des, vor fi "+str(max_index)+" asi")
#7
prob_esec_1=5/6
prob_esec_2=35/36
if(prob_esec_1**4>prob_esec_2**24):
    print("Pariu pe dubla")
else:
    print("Pariu pe simplu")