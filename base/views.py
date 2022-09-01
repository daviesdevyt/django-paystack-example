import imp
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_public_key(request):
    return JsonResponse(settings.PAYSTACK_PUBLIC_KEY, safe=False)