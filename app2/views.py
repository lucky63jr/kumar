from django.shortcuts import render

# Create your views here.
def app2(request):
    d={'a':500,'b':1000,'c':250,'name':'lucky'}
    return render(request,'a2.html',context=d)
