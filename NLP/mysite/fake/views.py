from django.shortcuts import render
from django.conf.urls.static import static
import pickle
import re
import string
import random

import fake

# Create your views here.

def pak(request):
    return render(request , 'index.html')

def news(request):
    
    # a=dict()
    # print(request.method)
    # if(request.method == 'POST'):
    #     dict1=request.POST
    #     print(dict1)
    #     dict1=dict(dict1.dict())
    #     a['text']=dict1['paragraph']
    #     a=a['text']
        
    data = random.uniform(0,1) 

    if(data>0.5):
        data =True

    else:
        data = False 


    return render(request,'index2.html',{'data':data})
