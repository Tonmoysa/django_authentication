from django.shortcuts import render

# Create your views here.

def index(request):
    diction={}
    return render(request, 'login_app/index.html',context=diction)
