from django.contrib import admin

from .models import Author, Book, Rating


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ["title", "author"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ["forename", "surname"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["book", "stars", "rating"]
