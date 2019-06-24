

#from django.shortcuts import render_to_resp

from django.http.response import HttpResponse


def index(request):
 #   txt=request.GET['txt']
  #  context={}
   # if txt=='1':
    #context['condition 1'] = True
    #else txt=='2':
     #   context['condition 2']=True
   return HttpResponse(b'Hello World')
    #return render_to_response('index.html',context)