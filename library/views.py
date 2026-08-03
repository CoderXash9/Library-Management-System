from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


class IssueBookAPIView(APIView):

    def post(self, request):

        book_id = request.data.get("book")
        member_id = request.data.get("member")

        if not book_id or not member_id:
            return Response(
                {"error": "Book ID and Member ID are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        book = get_object_or_404(Book, id=book_id)
        member = get_object_or_404(Member, id=member_id)

        if book.available_copies <= 0:
            return Response(
                {"error": "Book is currently unavailable."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        existing_issue = IssueRecord.objects.filter(
            book=book, member=member, status="Issued"
        ).exists()

        if existing_issue:
            return Response(
                {"error": "This member already has this book issued."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        issue = IssueRecord.objects.create(
            book=book,
            member=member,
        )

        book.available_copies -= 1
        book.save()

        return Response(
            {
                "message": "Book issued successfully.",
                "issue_id": issue.id,  # type: ignore
            },
            status=status.HTTP_201_CREATED,
        )

class ReturnBookAPIView(APIView):

    def post(self,request):

        issue_id = request.data.get("issue_id")

        if not issue_id:
            return Response(
                {"error" : "Issue ID is required"},
                status = status.HTTP_400_BAD_REQUEST
            )
