from django.urls import path, include
from . import views, api
from rest_framework import routers


app_name = "encadenes"
router = routers.DefaultRouter()

router.register('v1', api.RouteViewSet, 'routes')

urlpatterns = [
     # ex: /encadenes/
    path("", views.mainView, name="index"),
    # ex: /encadenes/crags
    path("crags/", views.CragsView.as_view(), name="crags"),
    path("routes/", views.RoutesView.as_view(), name="routes"),
    path("sectors/", views.SectorsView.as_view(), name="sectors"),
    path("api/", include(router.urls))
]