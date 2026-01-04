from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from basic.models import Book,userData,MovieBooking
import json

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

# Data inserting into DATABASE___________________________________________________________________________________
@csrf_exempt
def dataInsert(request):
    try:
        if request.method == "POST":

            data = json.loads(request.body)
            print(data)
            name = data.get("name")
            age = data.get("age")
            branch = data.get("branch")
            userData.objects.create(name=name, age=age, branch=branch)
        return JsonResponse({"status":"successful", "data":data, "status_code": 201},status=201)
    except Exception as e:
        return JsonResponse({'status':'failed',"error":str(e),"status_code": 500},status=500)


# Adding movie details into DATABASE________________________________________________________________________
@csrf_exempt
def movieInsert(request):
    try:
        if request.method == "POST":

            data = json.loads(request.body)
            print(data)

            moviename = data.get("moviename")
            genre = data.get("genre")
            showtime = data.get("showtime")
            screenname = data.get("screenname")

            MovieBooking.objects.create(moviename=moviename, genre=genre, showtime=showtime, screenname=screenname)

            return JsonResponse(
                {"status": "successful", "data": data, "status_code": 201},status=201)

        return JsonResponse({"status": "failed", "message": "Only POST method allowed"}, status=405)

    except Exception as e:
        return JsonResponse({"status": "failed","error": str(e),"status_code": 500},status=500)

# Get Movies by GENRE_______________________________________________________________________________________
def getMoviesByGenrename(request,genre):
    try:
        if request.method=="GET":
            data=MovieBooking.objects.filter(genre=genre).values()           
            final_data=list(data) 
            if len(final_data)==0:
                msg="no records found"
            else:
                msg="Records fetched successfully"          
            return JsonResponse({"status":"success","msg":msg,genre:final_data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"})


# Updating Movie Screens by using update___________________________________________________________

@csrf_exempt
def updateMovieScreen(request):
    try:
        if request.method=="PUT":
            input_data = json.loads(request.body)
            old_screen = input_data['old_screen']
            new_screen = input_data['new_screen']
            data=MovieBooking.objects.filter(screenname=old_screen).update(screenname=new_screen) 
            print(data)
            if data==0:
                msg="no records found"
            else:
                msg="Records updated successfully"          
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure","msg":"only PUT method allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error",str(e):"something went wrong"},status=500)


# CRUD for Book Model_______________________________________________________________________
@csrf_exempt
def bookInsert(request):
    try:
        if request.method == "POST":
            try:
                input_data = json.loads(request.body)
                book_name = input_data["bookname"]
                book_price = input_data["bookprice"]
                author = input_data["author"]
                book_type = input_data["booktype"]
                Book.objects.create(bookname = book_name, bookprice = book_price, author = author, booktype = book_type)
                return JsonResponse(
                    {"status": "successful", "data": input_data, "status_code": 201},status=201)
            except Exception as e:
                return JsonResponse({"status": "failed", "message": "Only POST method allowed"}, status=405)


        elif request.method == "GET":
            try:
                data=Book.objects.filter().values()           
                final_data=list(data) 
                if len(final_data)==0:
                    msg="no records found"
                else:
                    msg="Records fetched successfully"          
                return JsonResponse({"status":"success","msg":msg,"book":final_data},status=200)
            except Exception as e:
                return JsonResponse({"status":"failure","msg":"only GET method allowed"},status=400)
        

        elif request.method == "PUT":
            try:
                input_data = json.loads(request.body)
                bookid = input_data['id']
                name = input_data['bookname']
                price = input_data['bookprice']
                author = input_data['author']
                booktype = input_data['booktype']
                data=Book.objects.filter(id=bookid).update(bookname=name, bookprice=price, author=author, booktype = booktype)           
                final_data=list(input_data) 
                if len(final_data)==0:
                    msg="no records found"
                else:
                    msg="Records fetched successfully"          
                return JsonResponse({"status":"success","msg":msg,"book":final_data},status=200)
            except Exception as e:
                return JsonResponse({"status":"failure","msg":"only PUT method is allowed"},status=400)


        elif request.method == "DELETE":
            try:
                input_data = json.loads(request.body)
                delete_id = input_data["id"]
                data = Book.objects.filter(id = delete_id).delete()
                print(data)
                if data[0]==0:
                    msg="No record found"
                else:
                    msg = "record deleted successfully"
                return JsonResponse({"status":"success","msg":msg},status=200)
            except Exception as e:
                return JsonResponse({"status":"failure","msg":"only DELETE method is allowed"},status=400) 


    except Exception as e:
        return JsonResponse({"status":"error",str(e):"something went wrong"},status=500)