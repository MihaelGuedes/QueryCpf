from django.db import models
from cpf_field.models import CPFField
from django.db.models.fields import FloatField, IntegerField

class Person(models.Model):
    cpf = CPFField('cpf', unique=True)
    scale = IntegerField(blank=False)
    score = FloatField(null=True)

    def __str__(self):
        return self.cpf


    class Meta:
        verbose_name = u'Pessoa'
        verbose_name_plural = u'Pessoas'
