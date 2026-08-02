from rest_framework import serializers
from .models import Author, Member, Book, IssueRecord


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = "__all__"


class IssueRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueRecord
        fields = "__all__"
