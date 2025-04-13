from django.db import models
from django . utils import timezone
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150, unique=True, null=True)
    email = models.EmailField(max_length=150, unique=True, null=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=150)

class Book(models.Model):
    title = models.CharField(max_length=150, null=True)
    rating = models.IntegerField(null=True)
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    
class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
    