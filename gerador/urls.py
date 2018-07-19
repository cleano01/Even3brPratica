from django.conf.urls import url
from gerador import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^email/', views.email, name='email'),
]