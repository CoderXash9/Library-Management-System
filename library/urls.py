from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AuthorViewSet,
    MemberViewSet,
    BookViewSet,
    IssueRecordViewSet,
)

router = DefaultRouter()  # creating the object for the routers

router.register("authors", AuthorViewSet)
router.register("members", MemberViewSet)
router.register("books", BookViewSet)
router.register("IssueRecords", IssueRecordViewSet)

urlpatterns = [path("", include(router.urls))]
