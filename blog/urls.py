from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='blog'),
    path('test/', views.test, name='test')
]