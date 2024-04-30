# from django.conf.urls import url
from django.urls import path
from .views import (
    CustomerListApiView
)

urlpatterns = [
    path('api', CustomerListApiView.as_view())
]