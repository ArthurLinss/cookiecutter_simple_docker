# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Author(models.Model):
    forename = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.forename + " " + self.surname

    def get_name(self):
        return self.forename + " " + self.surname


class Book(models.Model):
    """
    model for books
    """

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default="")
    author = models.ForeignKey(Author, default=None, on_delete=models.CASCADE)

    status_choices = [
        ("Unread", "Unread"),
        ("Read", "Read"),
    ]

    status = models.CharField(
        max_length=6,
        choices=status_choices,
        default="Unread",
    )

    def __str__(self):
        return self.title + " by " + self.get_author()

    def get_author(self):
        return self.author.get_name()


class Rating(models.Model):
    """
    model for rating of book
    """

    rating = models.TextField(default="")
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)

    star_choices = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]

    stars = models.CharField(
        max_length=1,
        choices=star_choices,
        default="1",
    )

    def __str__(self):
        return self.rating
