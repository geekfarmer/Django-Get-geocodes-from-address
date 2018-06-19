from django.conf.urls import url

from . import views

app_name = "Getaddress"

urlpatterns = [
    url('', views.index, name='index'),
]
