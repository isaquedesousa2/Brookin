from django.contrib import admin
from .models import User
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import admin as admin_user 

@admin.register(User)
class UserAdmin(admin_user.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    models = User