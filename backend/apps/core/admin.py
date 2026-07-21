from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom User Admin with role-based display.
    """
    list_display = ('username', 'get_full_name', 'email', 'phone_number', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'is_phone_verified', 'created_at')
    search_fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')
    ordering = ('-created_at',)
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'phone_number', 'is_phone_verified')
        }),
    )

    def get_full_name(self, obj):
        return obj.get_full_name() or 'N/A'
    get_full_name.short_description = 'To\'liq Ismi'
