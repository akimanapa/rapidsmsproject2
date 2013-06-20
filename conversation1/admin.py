from django.contrib import admin
from conversation1.models import Questions

#admin.site.register(Questions)
class ConvAdmin(admin.ModelAdmin):
    #fields = ['question', 'reponse']
    fields = ['question']

admin.site.register(Questions, ConvAdmin)
