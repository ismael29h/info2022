from django.contrib import admin

from .models import Post

#para mayores detalles en el panel de administración
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_added')
    #list_filter = ()
    search_fields = ['title', 'intro', 'body']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
