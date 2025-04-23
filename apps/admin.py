from django.contrib import admin
from .models import MyModel

# Register your models here.
@admin.register(MyModel)

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # Replace with your model's fields
    search_fields = ('field1', 'field2')  # Replace with searchable fields
    list_filter = ('field3',)  # Replace with fields to filter by
admin.site.register(MyModel)