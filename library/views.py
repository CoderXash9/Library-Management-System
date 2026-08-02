from rest_framework import viewsets

from .models import Author, Member, Book, IssueRecord
from .serializers import (
    AuthorSerializer,
    MemberSerializer,
    BookSerializer,
    IssueRecordSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class IssueRecordViewSet(viewsets.ModelViewSet):
    queryset = IssueRecord.objects.all()
    serializer_class = IssueRecordSerializer
