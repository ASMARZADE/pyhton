#task 1
'''from math import *
def koordinat(x,y):   
    return y<=4-abs(x) and y>=cos(2*x) and (y-10)**10 +(x+4)**10<=100 or (y-1)**2+(x-3)**2<=4 and y>=cos(2*x)and (x<3 or y>=4-abs(x))
x,y=map(float,input('Koordinatlari daxil edin:').split(' '))
print(f'verilmis ededler oblasta daxildir ' if koordinat(x,y) else f' verilmis ededler oblasta daxil deyil' )
'''    
#Task 2:
'''def sade(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def req_cem(eded):
    s=0
    while eded!=0:
        s+=eded%10
        eded//=10
    return s

from random import randint
N=int(input('Uzunluqu daxil edin: '))
List1=[randint(20,50) for _ in range(N)]
print(f'List->{List1}')
print('Reqemleri cemi sade olan ededler:')
List2=[]
for i in List1:
    if sade(req_cem(i)):
        List2+=[i]
print(f'Yeni list->{List2}')'''
#TASK 3
'''setir=input('Setri :')
axtarilan_soz=input('Axtarilan  soz:')
say=0
for i in range(len(setir)-len(axtarilan_soz)):
    if setir[i:i+len(axtarilan_soz)]==axtarilan_soz:
        say+=1
print(f'{axtarilan_soz} simvollarin umumi sayi {say}')'''
#task 4
'''n=int(input("n heddini daxil edin:"))
x=float(input("x ededdini daxil edin:"))
cem=0
hasil=1
for j in range(1,n+1):
    hasil*=j
    cem+=x**j/hasil
print(f'Netice: {cem:.3f}')'''
#task 5
'''def Bolenler(eded):
    s=0
    for i in range(1,eded+1):
        if eded%i==0:
            s+=1
    return s
def kv_cem(eded):
    s=0
    while eded!=0:
        s+=(eded%10)**2
        eded//=10
    return s

from random import randint
N=int(input('Siyahinin uzunluqu N: '))
List1=[randint(10,99) for _ in range(N)];List1_bolenler=[]
List2=[]
List2_bolenler=[]
for i in List1:
    List1_bolenler+=[Bolenler(i)]
for k in List1:
    List2+=[kv_cem(k)]
for j in List2:
    List2_bolenler+=[Bolenler(j)]
print(f'List1 = {List1}   List1_bolenler = {List1_bolenler}')
print(f'List2 = {List2}   List2_bolenler = {List2_bolenler}')
Cutler=[]
for i in range(N):
    Cutler+=[(List1_bolenler[i],List2_bolenler[i])]
print()
print(f'Cutler = {Cutler}')
Muqayise=[]
b=0;s=0
for i in Cutler:
    if i[0]>=i[1]:
        Muqayise+=[1]
        b+=1
    else:
        Muqayise+=[0]
        s+=1
print(f'Muqayise: {Muqayise}')
print()
if b>s:
    print('Netice: List1-de bolenlerin sayi cox olan ededlerin sayi daha coxdu')
else:
    print('Netice: List2 de bolenlerin sayi cox olan ededlerin sayi daha coxdu')
'''
#task 6
'''def req_cem(eded):
    s=0
    while eded!=0:
        s+=eded%10
        eded//=10
    return s

def req_ferq(eded):
    return eded//100-eded%10-(eded//10)%10

from random import choice
def quickSort(A):
    if len(A)<=1:
        return A
    X=choice(A)
    B1=[b for b in A if b<X]
    BX=[b for b in A if b==X]
    B2=[b for b in A if b>X]
    return quickSort(B1)+BX+quickSort(B2)

def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-2,i-1,-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

def selectionSort(A):
    for i in range(len(A)-1):
        Min=i
        for k in range(i+1,len(A)):
            if A[k]<A[Min]:
                Min=k
        if Min!=i:
            A[i],A[Min]=A[Min],A[i]
    return A

from random import randint
N=int(input('Siyahinin uzunluqu N: '))
A1=[randint(100,999) for i in range(N)]
A2=[req_cem(i) for i in A1]
A3=[req_ferq(i) for i in A1]
print(f'A1 = {A1}\nA2 = {A2}\nA3 = {A3}\n')
print('Sort alqoritmleri tetbiq edildikden sonra:\n')
print(f'A1 = {bubbleSort(A1)}\nA2 = {selectionSort(A2)}\nA3 = {quickSort(A3)}')

'''

#task 7
'''from random import randint
N=int(input('matrisin olcusu N-I daxil edin '))
Matris=[[randint(10,99) for _ in range(N)] for _ in range(N)]
print('A matris:\n')
for i in range(N):
    for j in range(N):
        print(Matris[i][j],end='\t')
    print()
print('\nB matrisi: ')
for i in range(N):
    for j in range(N):
        if i>j:
            print('BBB',end='\t')
        elif i<j:
            print('AAA',end='\t')
        else:
            print(Matris[i][j],end='\t')
    print()
print()

maxMatris = Matris[0][0]
for i in range(len(Matris)):
    if Matris[i][i] >= maxMatris:
        maxMatris = Matris[i][i]
        indeks=(i,i)
print(f'Minimal element = {maxMatris}, index = {indeks}')'''












































    

    
























    
    





































































































    
    
