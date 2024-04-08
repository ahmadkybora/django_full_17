from django.urls import path
from .views import index, show

urlpatterns = [
    path('', index, name='index'),
    path('show/pk<int:id>', show, name='show')
]