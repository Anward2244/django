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

# HTTP response_______________________________________________________
def htres(request):
    return HttpResponse('hello')

# Json response____________________________________________________
def jsres(request):
    info = {"data":[{
        "name": "Anwar",
        "age": "22"
    }]}
    return JsonResponse(info)

# Query params_______________________________________________________
def getreq(request):
    name = request.GET.get('name') 
    city = request.GET.get('city')
    return HttpResponse(f'hello {name}, you are from {city}.')

# Filtering Data______________________________________________________
def cityfil(request):
    info = [{'name':'Anwar','city':'hyd'},{'name':'Shasha','city':'hyd'},{'name':'Hussain','city':'banglore'},{'name':'Sagar','city':'banglore'}]
    fildata = []
    city = request.GET.get('city')
    for i in info:
        if i['city'] == city:
            fildata.append(i)
    
    return JsonResponse({'data':fildata})

#pagination logic________________________________________________________
def pages(request):
    limit = int(request.GET.get("limit", 4))
    page = int(request.GET.get("page", 1))

    items = list(range(1, 21))

    total_items = len(items)
    if (total_items % limit) == 0:
        total_pages = (total_items // limit)
    else:
        total_pages = (total_items // limit) + 1

    start = (page - 1) * limit
    end = start + limit
    page_data = items[start:end]

    return JsonResponse({"limit": limit, "total_pages": total_pages,"current_page": page, "data": page_data,})
