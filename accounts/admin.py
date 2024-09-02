from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'user_type', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ('user_type','is_admin', 'is_active')
    fieldsets = ()
    search_fields = ('email', 'username', 'first_name', 'last_name')

    # Add additional fields for the account creation form
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name', 'last_name', 'username', 'user_type', 'password1', 'password2'),
    #     }),
    # )



admin.site.register(Account, AccountAdmin)

