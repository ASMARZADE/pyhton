#1
'''a='Dersim azdir'
b=input()
s=0
for i in a:
    if b==i:
        s=s+1
if s>0:
    print(f'{b} simvolu {a} metninde movcuddur')
else:
    print(f'{b} simvolu {a} metninde movcud deyil')'''
#2
'''def evezetme(setir):
    yeni=''
    for herf in setir:
        if herf=='a':
            yeni=yeni+'b'
        elif herf=='A':
            yeni=yeni+'B'
        elif herf=='B':
            yeni=yeni+'A'
        elif herf=='b':
            yeni=yeni+'a'
        else:
            yeni=yeni+herf
    return yeni
print(evezetme(input('setir daxil edin: ')))'''
#3
'''def uzunluq(setir):
    s=0
    for i in setir:
        s=s+1
    return s
def soz_sayi(setir):
    setir=setir+' '
    soz=0
    for j in range(uzunluq(setir)):
        if setir[j]!=' ' and setir[j+1]== ' ' :
            soz=soz+1
    return soz
print(soz_sayi(input('setir daxil edin: ')))'''
#4
'''def uzunluq(setir):
    s=0
    for i in setir:
        s=s+1
    return s
def enuzun(setir):'''
#5
'''a=input('soyad,ad,ata adi daxil edin: ')
b=a.split()
ad=b[1]
ata_adi=b[2]
print(f'{ad[0]}.{ata_adi[0]}.{b[0]}')'''
#6
'''fayl=input('faylin unvanini daxil edin: ')
b=fayl.split('/')
for i in b:
    print(i,'\n')'''
#7
'''def uzunluq(a):
    s=0
    for herf in a:
        s=s+1
    return s
def evezetme(setir,a,b):
    i=0
    yeni=''
    while i<uzunluq(setir):
        if setir[i:i+uzunluq(a)]==a:
            yeni=yeni+b
            i=i+uzunluq(a)
        else:
            yeni=yeni+setir[i]
            i=i+1
    return yeni
print(evezetme(input('setir daxil edin: '),input('evez edilen:: '),input('evez eden: ')))'''
#8
'''def uzunluq(simvol):
    s=0
    for herf in simvol:
        s=s+1
    return s
def simv_sayi(setir,simvol):
    i=0
    say=0
    while i<uzunluq(setir):
        if setir[i:i+uzunluq(simvol)]==simvol:
            say+=1
            i=i+uzunluq(simvol)
        else:
            i=i+1
    return say
print(simv_sayi(input('setir daxil edin: '),input('axtarilan simvol: ')))'''
#9
'''def uzunluq(a):
    s=0
    for herf in a:
        s=s+1
    return s
setir='Bayram günü gələcəyik sizə bayramlaşmağa. Bayramlaşsaz da bayramlaşacağıq. Bayramlaşmasanız da bayramlaşacağıq.'
i=0
say=0
yeni=''
while i<uzunluq(setir):
        if setir[i:i+uzunluq('bayram')]=='bayram' or setir[i:i+uzunluq('bayram')]=='Bayram':
            yeni=yeni+'novruz'
            i=i+uzunluq('bayram')
            say+=1
        else:
            yeni=yeni+setir[i]
            i=i+1
print(yeni,say)'''
#10
'''def uzunluq(a):
    s=0
    for herf in a:
        s=s+1
    return s
setir='Haqqı, haqqıya getmiş, Haqqı, haqqıdan haqqını istəmiş, Haqqı, Haqqının haqqını verməyincə, Haqqı da Haqqının haqqından gəlmiş.'
i=0
say=0
yeni=''
while i<uzunluq(setir):
        if setir[i:i+uzunluq('haqqı')]=='haqqı' or setir[i:i+uzunluq('haqqı')]=='Haqqı':
            yeni=yeni+'sarı'
            i=i+uzunluq('haqqı')
            say+=1
        else:
            yeni=yeni+setir[i]
            i=i+1
print(yeni,say)'''
#11
'''def uzunluq(a):
    s=0
    for herf in a:
        s=s+1
    return s
def herf2_sil(cumle):
    yeni=''
    soz=''
    cumle=cumle+' '
    for i in range(uzunluq(cumle)):
        if cumle[i]!=' ':
            soz=soz+cumle[i]
        else:
            yeni=yeni+soz[0]+soz[2:]+' '
    return yeni
print(herf2_sil(input('cumle daxil edin: ')))'''
#12
'''sait="AOUE"
samit='bcmf'
reqem='3579'
durgu='!?,;'
setir='Ay ana, Ayan 5-ci kitabi oxumaga imkan vermir!'
for i in sait:
    for j in setir:
        if i==j:
            print(i,end=' ')
            break
for i in samit:
    for j in setir:
        if i==j:
            print(i,end=' ')
            break        
for i in reqem:
    for j in setir:
        if i==j:
            print(i,end=' ')
            break
for i in durgu:
    for j in setir:
        if i==j:
            print(i,end=' ')
            break
print('simvollari var',end=' ')'''
#13
'''ifade=input('ifadeni daxil edin: ')
a=ifade.split('+')
cem=0
for i in a:
    cem+=int(i)
print(cem)'''
#14
'''def uzunluq(ifade):
    s=0
    for i in ifade:
        s=s+1
    return s
ifade=input('ifade daxil edin: ')
i=0
yeni=''
while i<uzunluq(ifade):
    if ifade[i]!='+' and ifade[i]!='-':
        yeni=yeni+ifade[i]
        i=i+1
    elif ifade[i]=='-' or ifade[i]=='+' :
        yeni=yeni+' '
        i=i+1
eded=yeni.split(' ')
cavab=int(eded[0])
n=0
for i in range(len(ifade)):
    if ifade[i]=='-':
        cavab=cavab-int(eded[n+1])
        n=n+1
    elif ifade[i]=='+':
        cavab=cavab+int(eded[n+1])
        n=n+1

print(cavab)'''
#15
'''def funksiya(setir):
    soz_1=''
    for i in range(len(setir)):
        if setir[i]!=' ':
            soz_1=soz_1+setir[i]
        else:
            break
    return soz_1
print(funksiya(input('cumleni daxil edin: ')))'''
#16
'''def uzunluq(setir):
    s=0
    for i in setir:
        s=s+1
    return s
def funksiya(ad,genis):
    yeni=''
    n=0
    for i in range(len(ad)):
        if ad[i]=='.':
            n=n+1
    if n==0:
        yeni=ad+'.'+genis
    else:
        add=ad.split('.')
        j=0
        while j<(uzunluq(add)-1):
            yeni=yeni+add[j]+'.'
            j=j+1
        yeni=yeni+genis
    return yeni
print(funksiya(input('faylin adini daxil edin: '),input('faylin yeni genishlenmesini daxil edin: ')))'''
#17
'''def uzunluq(setir):
    s=0
    for i in setir:
        s=s+1
    return s
ad=input('excel faylinin adini daxil edin: ')
simvol='/\*?''<>|'
if uzunluq(ad)>10:
    print('faylin adinda 10-dan artiq simvol ola bilmez')
else:
    for i in ad:
        for j in simvol:
            if i==j:
                print(f'faylin adinda {simvol} simvollari ola bilmez')'''
#18
'''def uzunluq(ad):
    s=0
    for i in ad:
        s=s+1
    return s
ad=input('qovlugun adi: ')
boyuk='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
kicik='abcdefghijklmnopqrstuvwxyz'
xususi='.-~:=_'
reqem='1234567890'
boy=0
kic=0
xus=0
req=0
for i in ad:
    for j in boyuk:
        if i==j:
            boy=boy+1
    
    for m in kicik:
        if i==m:
            kic=kic+1
    
    for s in xususi:
        if i==s:
            xus=xus+1
    
    for k in reqem:
        if i==k:
            req=req+1
if 5>uzunluq(ad)or uzunluq(ad)>15:
    print('5<=simvol sayi<=15 olmalidir')
if kic==0:
    print('Yanlis!En az 1 kicik herf olmalidir!')
if boy==0:
    print('Yanlis!En az 1 boyuk herf olmalidir!')
if req==0:
    print('Yanlis!En az 1 reqem olmalidir!')
if xus==0:
    print('Yanlis!En az 1 xususi simvol olmalidir!')
if kic!=0 and boy!=0 and req!=0 and xus!=0 and 5<=uzunluq(ad)<=15:
    print('Duzgun qovluq adi!')'''


    


























            
            
        










































            
            
        


































            


























            
            
        
        
        
    






                     
                     
                     
    
    
    
    
    

























            
            
        
    
