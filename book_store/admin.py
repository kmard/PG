from django.contrib import admin

from book_store.models import Book,Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    #
    # prepopulated_fields = {'slug':('title',)}
    #
    list_display = ('title','author','rating')

    list_filter = ('title','author')
    pass

admin.site.register(Book,BookAdmin)
admin.site.register(Author)