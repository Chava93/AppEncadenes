from django.urls import path
from . import views

app_name = "encadenes"

urlpatterns = [
     # ex: /encadenes/
    path("", views.mainView, name="index"),
    # ex: /encadenes/crags
    path("crags/", views.CragsView.as_view(), name="crags"),
    path("routes/", views.RoutesView.as_view(), name="routes"),
    path("sectors/", views.SectorsView.as_view(), name="sectors"),
]