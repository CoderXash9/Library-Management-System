from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet

router = DefaultRouter()  # creating the object for the routers

router.register("authors", AuthorViewSet)

urlpatterns = [path("", include(router.urls))]
