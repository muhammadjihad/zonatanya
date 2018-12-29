from django.urls import path, re_path
from . import views


app_name = 'penanya'
urlpatterns=[
	re_path(r'^detail/(?P<slugInput>[\w-]+)/$',views.detail),
	path('jawab/',views.jawab, name = 'formjawab'),
	path('',views.index),
]