from django.contrib import admin
from .models import Tutorial, Book, Tutor, BlogPost, Vacancy

# Register your models here.
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role', 'address', 'phone')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'role', 'password1', 'password2', 'address', 'phone'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'role')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade_level', 'subject', 'created_at')
    search_fields = ('title', 'description', 'subject')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author', 'description')

class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'contact_info', 'created_at')
    search_fields = ('name', 'subject', 'contact_info')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author', 'content')

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('position', 'institution', 'application_deadline', 'created_at')
    search_fields = ('position', 'institution', 'description')

admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Vacancy, VacancyAdmin)
