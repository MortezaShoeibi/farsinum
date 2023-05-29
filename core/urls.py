from django.urls import path
from core import views

app_name: str = 'core'

urlpatterns: list = [
    path('converter', views.NumberToText.as_view(), name='number_to_text'),
]
