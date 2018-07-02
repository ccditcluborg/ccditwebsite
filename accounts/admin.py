from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'first_name', 'last_name', 'student_number', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'student_number', 'password')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'student_number', 'password1', 'password2')
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name', 'student_number')
    ordering = ('first_name', 'last_name')
    filter_horizontal = ()

admin.site.register(User, UserAdmin)