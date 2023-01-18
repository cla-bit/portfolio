from django.contrib import admin
from .models import Project, Category, Contact, Portfolio, Skills, Services

# Register your models here.


@admin.register(Skills)
class SkillsInline(admin.ModelAdmin):
    list_display = ['skills']


@admin.register(Services)
class ServicesInline(admin.ModelAdmin):
    list_display = ['services']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number', 'cv']
    filter_horizontal = ['skills', 'services']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'name_slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
