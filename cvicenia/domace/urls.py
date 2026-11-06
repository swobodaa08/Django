from django.urls import path
from . import views

urlpatterns = [
    path('meno/', views.meno, name='meno'),
]
