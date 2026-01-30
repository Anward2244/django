import json
from django.http import JsonResponse
import re
from basic.models import User

class authMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.username_pattern = re.compile(r'^[a-zA-Z0-9_]{5,15}$')
        self.email_pattern = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$')
        self.password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#]{8,}$')
    def __call__(self,request):
        if request.path in ['/login/', '/signup/'] and request.method == "POST":
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"error":"invalid JSON data"}, status = 400)

            if request.path == "/signup/":
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")

                if not all ([username,email,password]):
                    return JsonResponse({"error":"All fields are required"}, status = 400)

                if not self.username_pattern.match(username):
                    return JsonResponse({"error":"Invalid username format"}, status = 400)

                if not self.email_pattern.match(email):
                    return JsonResponse({"error":"Invalid email format"}, status = 400)

                if not self.password_pattern.match(password):
                    return JsonResponse({"error":"Invalid password format"}, status = 400)

                if User.objects.filter(username=username).exists():
                    return JsonResponse({"error":"Username already exists"}, status = 400)

                if User.objects.filter(email=email).exists():
                    return JsonResponse({"error":"Email already exists"}, status = 400)

            if request.path == "/login/":
                username = data.get("username")
                password = data.get("password")

                if not all ([username,password]):
                    return JsonResponse({"error":"Username and Password are required"}, status = 400)

                try:
                    user = User.objects.get(username=username)
                except user.DoesNotExist:
                    return JsonResponse({"error":"invalid username"},status=401)
                
                if user.password != password:
                    return JsonResponse({"error":"invalid password"},status=401)

        response = self.get_response(request)
        return response