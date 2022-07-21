import logging

from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger(__name__)


def index(request):
    test_var = settings.TEST_VAR
    logger.info(f"TEST_ENV_VAR --> {test_var}")
    return HttpResponse(f"Posts index view.\nTest variable name: {test_var}.")


def post(request):
    if request.POST:
        data = request.POST.dict()
        for key, value in data.items():
            logger.info(f"POST param: {key} = {value}")

        return HttpResponse("<h1>It's POST method for 'posts'</h1>")

    data = request.GET.dict()

    text_for_response = f"<h1>It's GET method for 'posts'</h1><p>Data:</p>"
    rows = [f"\n<br>{key} = {value}" for key, value in data.items()]
    text_for_response = text_for_response + "".join(rows)

    return HttpResponse(text_for_response)
