from django.contrib import admin
from .models import Members,Post,Topic

# Register your models here.

admin.site.site_header = '炎管家管理中心'
admin.site.site_title = '炎管家管理中心'
admin.site.index_title = '管理中心'


# 客製化欄位顯示
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'email', 'password', 'image', 'created_date', 'update_date')
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'title', 'content', 'created_date', 'update_date')
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_number', 'link','created_date', 'update_date', 'times')


# admin要註冊才可以管理這些Table
admin.site.register(Members, MembersAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)