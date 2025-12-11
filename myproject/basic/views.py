from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    
def services(request):
    return render(request, 'services.html')

def htres(request):
    return HttpResponse('hello')

def jsres(request):
    info = {"data":[{
        "name": "Anwar",
        "age": "22"
    }]}
    return JsonResponse(info)

def getreq(request):
    name = request.GET.get('name') 
    city = request.GET.get('city')
    return HttpResponse(f'hello {name}, you are from {city}.')

def cityfil(request):
    info = [{'name':'Anwar','city':'hyd'},{'name':'Shasha','city':'hyd'},{'name':'Hussain','city':'banglore'},{'name':'Sagar','city':'banglore'}]
    fildata = []
    city = request.GET.get('city')
    for i in info:
        if i['city'] == city:
            fildata.append(i)
    
    return JsonResponse({'data':fildata})