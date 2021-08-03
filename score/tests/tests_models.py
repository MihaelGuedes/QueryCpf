from django.test import TestCase
from model_mommy import mommy
from score.models import Person

class TestPerson(TestCase):
    def setUp(self):
        self.person = mommy.make(Person, cpf='115.409.790-08', scale=10, score=100)


    def test_person_creation(self):
        self.assertTrue(isinstance(self.person, Person))
        self.assertEquals(self.person.__str__(), self.person.cpf)

    def test_cpf_label(self):
        person = Person.objects.get(id=1)
        cpf_field = person.cpf
        self.assertEquals(cpf_field, '115.409.790-08')
    
    def test_cpf_label(self):
        person = Person.objects.get(id=1)
        scale_field = person.scale
        self.assertEquals(scale_field, 10)
    
    def test_score_label_not_null(self):
        person = Person.objects.get(cpf='115.409.790-08')
        score_field = person.score
        self.assertNotEquals(score_field, None)

    def test_updating_model(self):
        person = Person.objects.get(cpf='115.409.790-08')
        person.scale = 100
        person.save()
        response = person
        self.assertEquals(response.scale, 100)
