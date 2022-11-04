from django.contrib import admin

from blog.models import *

class postAdmin(admin.ModelAdmin):

    list_display = ('title','author','date')
    list_filter = ('title','author','tags')

    prepopulated_fields = {'slug':('title',)}
    # fields = ('title', 'excert', 'image_name','date','slug','content','author','tags')

class commentAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_email','post')

admin.site.register(Author)
admin.site.register(Post,postAdmin)
admin.site.register(Tag)
admin.site.register(Comment,commentAdmin)
