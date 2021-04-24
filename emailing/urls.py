from django.urls import path
from . import views

app_name = "emailing"

urlpatterns = [
    path("", views.contact_form, name="contact_form"),
    path("success/", views.sucessful_page, name="sucessful_page"),
]
