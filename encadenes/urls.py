from django.urls import path
from . import views

app_name = "encadenes"

urlpatterns = [
     # ex: /encadenes/
    path("", views.mainView, name="index"),
    # ex: /encadenes/crags
    path("crags/", views.CragsView.as_view(), name="crags")
]