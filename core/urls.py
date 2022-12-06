from django.urls import path
from .views import index, contato, produto, cliente

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('cliente/', cliente, name='cliente')
]
