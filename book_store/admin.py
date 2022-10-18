from django.contrib import admin

from book_store.models import Book,Author,Adress,Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    #
    # prepopulated_fields = {'slug':('title',)}
    #
    list_display = ('title','author','rating','is_bestselling')

    list_filter = ('title','author')


admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Adress)
admin.site.register(Country)