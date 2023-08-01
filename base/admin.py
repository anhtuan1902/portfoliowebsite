from django.contrib import admin
from .models import Category, Project, Skill, Contact


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'project_img', 'description', 'skills', 'link', 'start_project', 'end_project',
                    'active', 'created_date']
    list_filter = ['active', 'created_date']
    search_fields = ['id', 'title', 'skill']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project_img', 'active', 'created_date']
    list_filter = ['active', 'created_date']
    search_fields = ['id', 'name']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_skill', 'cate_skill', 'active', 'created_date']
    list_filter = ['active', 'created_date']
    search_fields = ['id', 'cate_skill']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'body', 'email', 'created_date']


admin.site.site_header = 'Portfolio Admin'
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact, ContactAdmin)
