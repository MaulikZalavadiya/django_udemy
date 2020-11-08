from django.contrib import admin
from .forms import StatusFrom
from .models import Status

# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['user','__str__','image']
    form = StatusFrom
    # class Meta:
    #     model = Status

admin.site.register(Status,StatusAdmin)