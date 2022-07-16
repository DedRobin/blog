from django.http import HttpResponse


def index(request):
    return HttpResponse("Posts index view")


def post(request):
    if request.GET.get("key") == "test":
        return HttpResponse("GET method for 'post'")
    if request.POST.get("key") == "test":
        return HttpResponse("POST method for 'post'")
