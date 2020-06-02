from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TourUser
from .forms import TourUserChangeForm, TourUserCreationForm


class TourUserAdmin(UserAdmin):
    add_form = TourUserCreationForm
    form = TourUserChangeForm
    model = TourUser
    list_display = ['email', 'first_name']
    fieldsets = (
        (None, {
            'fields': ('email', 'password'),
        }),
        ('Profile', {
            'fields': ('first_name', 'last_name', 'patronymic_name', 'gender', 'phone', 'birth_date')
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(TourUser, TourUserAdmin)
