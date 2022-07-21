import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def user(request):
    if request.POST:
        data = request.POST.dict()
        for key, value in data.items():
            logger.info(f"POST param: {key} = {value}")

        return HttpResponse("<h1>It's POST method for 'user'</h1>")

    data = request.GET.dict()

    text_for_response = f"<h1>It's GET method for 'user'</h1><p>Data:</p>"
    rows = [f"\n<br>{key} = {value}" for key, value in data.items()]
    text_for_response = text_for_response + "".join(rows)

    return HttpResponse(text_for_response)
