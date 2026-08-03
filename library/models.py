from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    membership_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICES = [
        ("Programming", "Programming"),
        ("Science", "Science"),
        ("History", "History"),
        ("Novel", "Novel"),
        ("Biography", "Biography"),
    ]

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    published_date = models.DateField()
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class IssueRecord(models.Model):
    STATUS_CHOICES = [
        ("Issued", "Issued"),
        ("Returned", "Returned"),
        ("Overdue", "Overdue"),
    ]

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="issue_records"
    )

    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="borrowed_books"
    )

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Issued")

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
