from rest_framework import serializers
from .models import Author, Member, Book, IssueRecord


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"
