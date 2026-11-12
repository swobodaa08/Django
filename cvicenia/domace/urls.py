from django.urls import path
from . import views

urlpatterns = [
    path('meno/', views.meno, name='meno'),
    path('vizitka/', views.du2_vizitka, name='du2_vizitka'),
]
