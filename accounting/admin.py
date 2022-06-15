from django.contrib import admin
from .models import Author, Book

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class PersonAuthor(admin.ModelAdmin):
    list_display = ("surname", "show_number_of_books")
    inlines = [
        BookInline,
    ]

    def show_number_of_books(self, obj):
        from django.utils.html import format_html

        result = Book.objects.filter(author=obj).count()
        return format_html("<b><i>{}</i></b>", result)
    show_number_of_books.short_description = "Количество книг"

admin.site.register(Book)







