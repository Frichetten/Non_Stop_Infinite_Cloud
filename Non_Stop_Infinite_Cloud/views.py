from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated():
        context = {'data': 'You are logged in ' + request.user.username}
    else:
        context = {'data': 'You are not logged in'}
    return HttpResponse("<h1>Home Page</h1>")
