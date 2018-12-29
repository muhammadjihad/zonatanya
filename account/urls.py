from django.urls import path
from django.contrib.auth import login

urlpatterns=[
	path('login/', login)
]