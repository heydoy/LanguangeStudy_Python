from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)   #admin.site.register를 써도 되지만 @데코레이터를 사용하면 좀더 간단 
class PostAdmin(admin.ModelAdmin) :
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug' : ('title',)}