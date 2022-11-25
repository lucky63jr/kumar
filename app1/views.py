from django.shortcuts import render

# Create your views here.
def app1(request):
    d={'a':500,'b':100}
    return render(request,'a1.html',context=d)