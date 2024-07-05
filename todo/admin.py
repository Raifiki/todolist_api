from django.contrib import admin

from todo.models import Todo



# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('created_at','title','description','user')

admin.site.register(Todo,TodoAdmin)
