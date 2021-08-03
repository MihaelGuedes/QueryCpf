from django.contrib import admin
from score.models import Person

class Persons(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'scale', 'score')
    list_display_links = ('id', 'cpf')
    search_fields = ('cpf', 'score')

admin.site.register(Person, Persons)