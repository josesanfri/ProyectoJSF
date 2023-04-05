from django.contrib import admin

from .models import ContactForm, JobApplication
# Register your models here

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_job', 'name', 'city', 'created')
    list_filter = ('type_job',)

admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(ContactForm)