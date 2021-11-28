from django.shortcuts import render
import random
from math import dist
from matplotlib import pyplot as plt
    
# Create your views here.
def home(request):

    return render(request,'index.html')

def tabla(request):
    umbral=0
    if request.method == 'GET':
        umbral=float(request.GET.get('u'))
    
    return render(request,'index.html',{'tabla':g_datos(umbral) })

def g_datos(umb):
    res=[]
    umbral= umb
    
    for i in range(10):
        x=[random.randrange(1,100)]
        y=[random.randrange(1,100)]
        euclidiana=(dist(x,y))
        
        if umbral >= euclidiana:
            a='No'
        else:
            a='Si'
        res.append([x,y,euclidiana,a])
        #res=([x,y])
        '''for j in res:
            plt.title('Distancia'+' '+str(j)+' '+a)
            plt.plot(j,'-g*')
            plt.show()
        '''
    return res

    



    

    
    


    
    
        


