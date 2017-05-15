from django.http import HttpResponse


# Create your views here.
def login(request):
    return HttpResponse("<h1>Login Page</h1>")
