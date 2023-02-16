from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingPage.as_view(), name='home'),
    path('all/', views.NGO_Directory.as_view(), name='ngo_directory'),
    path('ngos/<int:pk>/', views.NGO_Single.as_view(), name='ngo_single'),
]
