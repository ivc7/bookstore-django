from django.contrib import admin
from .models import Book, Author, BookOrder, Cart


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','price', 'stock', )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name')


@admin.register(BookOrder)
class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'cart', 'quantity')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'active', 'order_date')