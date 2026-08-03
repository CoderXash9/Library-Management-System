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


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):

        total = data.get("total_copies")
        available = data.get("available_copies")

        if total is not None and available is not None:
            if available > total :
                raise serializers.ValidationError(
                    {
                        "available_copies":
                        "Available copies cant be more than total copies."
                    }
                )

        return data
