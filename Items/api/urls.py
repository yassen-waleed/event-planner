from django.urls import path, include
from .views import ItemViewSet
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("items", ItemViewSet, basename="Items")


urlpatterns = [
    path('', include(router.urls)),
    path('types', views.all_type, name='view-types')
]
