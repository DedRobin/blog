from django.http import HttpResponse


def index(request):
    return HttpResponse("Posts index view")


def user(request):
    if request.GET.get("key") == "test":
        return HttpResponse("GET method")
    if request.POST.get("key") == "test":
        return HttpResponse("POST method")
