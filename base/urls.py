from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("public_key/", views.get_public_key),
    path("verify_transaction/", views.verify)
]