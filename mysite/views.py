
from django.http import HttpResponse

def hello_luke(request):
    return HttpResponse("Hello Luke")
