from django.contrib import admin

from DjangoWebAdvanced.web.models import Category, Todo


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
