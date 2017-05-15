from django.shortcuts import render


def home(request):
    context = {}
    if request.user.is_authenticated():
        context = {'data': request.user.username}
    return render(request, "home.html", context)

