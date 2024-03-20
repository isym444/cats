from django.urls import path

from mainsite import views

app_name = "mainsite"

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("about/", views.about.as_view(), name="about"),
]
