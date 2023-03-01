from django.contrib import admin
from .models import mydiary
 



# Register your models here
admin.site.register(mydiary)
class AdminMydiary(admin.ModelAdmin):
    list_display=['subject']

