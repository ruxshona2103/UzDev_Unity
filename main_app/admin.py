from django.contrib import admin
from .models import Category, Project, ProjectImage, NavItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'date', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'description', 'client')
    inlines = [ProjectImageInline]

@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('label', 'url')
    list_filter = ('is_active',)
    ordering = ('order',)