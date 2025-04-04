from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('edu/', views.initiatives, name='initiatives'),
    path('edu/pears/', views.pears, name='pears'),
    path('edu/diagnostic_test/', views.diagnostic_test, name='diagnostic_test'),
    path('edu/diagnostic_test/question/', views.test_question, name='test_question'),
]
