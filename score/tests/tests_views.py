from django.test import TestCase
from django.urls import reverse

class PersonDetailsTestCase(TestCase):

    def test_get_status_code_400(self):
        response = self.client.get(reverse('person_detail'))
        self.assertEquals(response.status_code, 400)
    
    def test_patch_status_code_404(self):
        response = self.client.patch(reverse('person_detail'))
        self.assertEquals(response.status_code, 404)
    
    def test_delete_status_code_404(self):
        response = self.client.delete(reverse('person_detail'))
        self.assertEquals(response.status_code, 404)
    
    def test_url(self):
        url = reverse('person_detail')
        self.assertEquals(url, '/score/')

''' Por conta de limitações em requisições com campos enviado no corpo da requisição,
    não foi possível realizar mais testes unitário, apenas os de caminhos ruins com status
    400 e 404.'''