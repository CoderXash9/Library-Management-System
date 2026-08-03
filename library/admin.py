from django.contrib import admin
from .models import Author, Member, Book, IssueRecord


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    search_fields = ("name", "email")
    ordering = ("name",)


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
    ordering = ("name",)


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
    ordering = ("title",)


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
        "book__title",
        "member__name",
    )
    list_filter = ("status",)
    ordering = ("-issue_date",)
