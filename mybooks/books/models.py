# from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    """
    model for books
    """

    title = models.CharField(max_length=100)
    author_forename = models.CharField(max_length=50, default="")
    author_surname = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title + " by " + self.get_author()

    def get_author(self):
        return self.author_forename + " " + self.author_surname
