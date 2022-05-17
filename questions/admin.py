from django.contrib import admin
from .models import Category, Comments, Answers, Questions

admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Answers)
admin.site.register(Questions)


