from rest_framework import serializers
from score import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
      model = models.Person
      fields = ['cpf', 'scale', 'score']
