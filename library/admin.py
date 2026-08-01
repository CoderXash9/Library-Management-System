from django.contrib import admin
from .models import Author, Book, Member, IssueRecord


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    search_fields = ("name", "email")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "membership_date",
        "is_active",
    )

    search_fields = ("name", "email", "phone")
    list_filter = ("is_active",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "genre",
        "available_copies",
        "total_copies",
    )
    search_fields = ("title", "isbn")
    list_filter = ("genre",)


@admin.register(IssueRecord)
class IssueRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "member",
        "issue_date",
        "due_date",
        "return_date",
        "status",
    )

    search_fields = (
        "book_title",
        "member_name",
    )

    list_filter = ("status",)
