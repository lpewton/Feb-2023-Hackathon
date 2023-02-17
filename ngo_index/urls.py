from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingPage.as_view(), name='home'),
    path('all/', views.NGO_Directory.as_view(), name='ngo_directory'),
    path('random/', views.NGO_Random.as_view(), name='random'),
    path('search/', views.SearchResults.as_view(), name='search_results'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('ngos/<int:pk>/', views.NGO_Single.as_view(), name='ngo_single'),
]
