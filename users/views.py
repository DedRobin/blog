import logging

from django.shortcuts import render
from django.http import HttpResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def user(request):
    if request.GET:
        data = request.GET.dict()
        logger.info(data)

        return HttpResponse(f"It's GET method for 'user'.\nData: {data}")

    if request.POST:
        data = request.POST.dict()
        logger.info(data)

        return HttpResponse(f"It's POST method for 'user'.\nData: {data}")
