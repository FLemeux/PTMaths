# views.py
from django.shortcuts import render,HttpResponse

def homepage_render(request):
     page=render(request,"index.html")
     return HttpResponse(page)


def cours_math_render(request):
     page=render(request,"cours_math.html")
     return page

def exo_math_render(request):
     page=render(request,"exo_math.html")
     return page

def DS_math_render(request):
     page=render(request,"DS_math.html")
     return page

def DM_math_render(request):
     page=render(request,"DM_math.html")
     return page

def info_render(request):
     page=render(request,"info.html")
     return page

def TP_render(request):
     page=render(request,"TP.html")
     return page

def colles_render(request):
     page=render(request,"colles.html")
     return page

def randompage_render(request):
     import random
     nb=random.randint(0,100)
     context={"nombre_alea":nb,"nombre_alea2":nb*2}
     page=render(request,"random.html",context)
     return page
