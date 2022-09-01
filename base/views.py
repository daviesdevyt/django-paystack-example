import imp
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from pypaystack import Transaction
import requests

# Create your views here.
def index(request):
    return render(request, "index.html")

def verify(request):
    ref = request.GET.get("reference")
    tx = Transaction(authorization_key=settings.PAYSTACK_PRIVATE_KEY).verify(ref)
    customer = tx[3]["customer"]
    email = customer['email']
    amount = tx[3]["requested_amount"]/100
    requests.get("https://paystack-api-785921875.development.catalystserverless.com/server/paystack_api/execute",
                params={"email":email, "ref":ref, "amount": amount})
    return JsonResponse(tx, safe=False)

def get_public_key(request):
    return JsonResponse(settings.PAYSTACK_PUBLIC_KEY, safe=False)