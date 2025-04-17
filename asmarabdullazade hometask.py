#6.Klaviaturadan 3 tam ədəd daxil edin, onların cəmini, hasilini və ədədi ortasını tapın.
'''a= int(input())
b= int(input())
c= int(input())
s=a+b+c
h=a*b*c
d= s/3
print("ededlerin cemi=",s)
print("ededlerin hasili=",h)
print("ededlerin ededi ortasi=",d)'''

#7Təsadüfi verilmiş dördrəqəmli ədədin bütün rəqəmlərinin kvadratları cəmini və  hasilini ekrana çıxaran proqram yazın.
'''from random import *
x=randint(1000,9999)
print("tesadufi ededi qeyd et=",x)
I=x//1000
q=I%1000
II=q//100
q=q%100
III=q//10
IV=q%10
h=I*II*III*IV
s=I**2+II**2+III**2+IV**2
print("ededlerin hasili=",h)
print("ededlerin kvadratlari cemi=",s)'''

#8.[6.5; 10.5] intervalındakı təsadüfi iki ədədin hasilini tapın. Nəticəni vergüldən  sonra 2 mərtəbə saxlamaqla yuvarlaqlaşdırın.
'''from random import uniform 
x=uniform(6.5,10.5)
y=uniform(6.5,10.5)
h=x*y
h=round(h,2)
print("ededlerin hasili = ",h)'''

#9.Təsadüfi seçilmiş beşrəqəmli ədədin rəqəmlərini və qarşısında kvadratlarını alt-alta ekrana çıxaran proqram yazın.
'''from random import *
x=randint(10000,99999)
I=x//10000
q=x%10000
II=q//1000
q=x%1000
III=q//100
q=x%100
IV=q//10
V=q%10

print(I,I**2)
print(II,II**2)
print(III,III**2)
print(IV,IV**2)
print(V,V**2)'''
#10.Cu tapsiriq  x və y (-1,1) intervalında təsadüfi həqiqi ədədlərdir. Verilmiş düstura əsasən a və b-nın  qiymətini vergüldən sonra 3 rəqəm saxlamaqla tapın.
#a=√(1+y^2 )*sin⁡〖x^2/(1+|y| )〗
#b=cos⁡(sin^2⁡(5*x)/√(|y| ))
'''from random import *
x=randint(-1,1)
y=randint(-1,1)
import math
a=math.sqrt(1+y**2)*math.sin(x**2/(1+abs(y)))
b=math.cos(math.sin(5*x)/math.sqrt(abs(y))**2)
print("{:8.3f}".format(a))
print("{:8.3f}".format(b))'''
#11Klaviaturadan üçrəqəmli ədəd daxil edin. Bütün rəqəmlərini vergül ilə ayiraraq ekrana çıxarın. (misal: daxil edilən: 345, ekrana çixan: 3,4,5) (hint: "/" klassik bölmə, "//" tam ədədli bölmə, "%" qalıq)
a=int(input())
I=a//100
q=a%100
II=q//10
III=q%10
print(I,II,III,sep=',')



      

