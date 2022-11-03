from django.urls import path
from django.views import View
from .views import *

urlpatterns = [
    path('', ListCategoria.as_view()),
    path('<int:pk>/', DetailCategoria.as_view()),
    path('create', CreateCategoria.as_view()),
    path('delete/<int:pk>', DeleteCategoria.as_view())
]

urlpatterns = [
    path('', ListTarefa.as_view()),
    path('<int:pk>/', DetailTarefa.as_view()),
    path('create', CreateTarefa.as_view()),
    path('delete/<int:pk>', DeleteTarefa.as_view())
]