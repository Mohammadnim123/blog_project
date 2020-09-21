from .views import HomePageView, PostDetailView
from django.urls import path

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('<int:pk>',PostDetailView.as_view(),name='details'),

]