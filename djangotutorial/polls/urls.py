from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("try/", views.test, name="test"),
    path("hello/", views.hello_page, name = "hello")
]