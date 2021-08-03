from django.urls import path
from score.views import person_detail

urlpatterns = [
    path('', person_detail.as_view(), name='person_detail'),
]