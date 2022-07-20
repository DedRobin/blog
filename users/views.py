import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def user(request):
    if request.POST:
        data = request.POST.dict()
        for k, v in data.items():
            logger.info("POST param: {} = {}".format(k, v))

        return HttpResponse("<h1>Data is recorded</h1>")

    data = request.GET.dict()

    return HttpResponse(f"It's GET method for 'user'.\nData: {data}")
