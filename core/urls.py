from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # Page d'accueil
    path('offres/', views.offres_list, name='offres_list'),
    path('offres/<slug:slug>/', views.offres_detail, name='offres_detail'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('mentions-legales/', views.mentions_legales, name='mentions_legales'),
    path('articles/', views.articles_list, name='articles_list'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
]
